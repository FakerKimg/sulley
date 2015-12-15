from sulley import *
from requests import base_http2_frame
import logging
import string
import random
import os
import csv
import datetime
import time

def check_ack_settings_frame(session, node, edge, sock):
    recv = session.last_recv
    if recv and recv[3] == '\x04' and recv[4] == '\x00':
        sock.send("\x00\x00\x00\x04\x01\x00\x00\x00\x00")

    if "\x00\x00\x00\x04\x01\x00\x00\x00\x00" not in recv:
        # Settings split
        try:
            recv = sock.recv(4096)
        except:
            pass

    return

def send_goaway_frame(sock):
    sock.send("\x00\x00\x08\x07" + ("\x00" * 13))

    return


# delete previous log file
try:
    os.remove("./fuzz_log")
except:
    pass

target_ip = "192.168.144.104"

sess = sessions.session(sleep_time = 0.001, logfile="./fuzz_log", logfile_level=logging.DEBUG, log_level=logging.DEBUG)
target = sessions.target(target_ip, 8080)
sess.add_target(target)

count = 10
wrong_methods = []
for i in range(0, count):
    length = random.randint(1, 10)
    wrong_methods.append(''.join(random.choice(string.uppercase) for i in range(length)))

wrong_schemes = []
for i in range(0, count):
    length = random.randint(1, 10)
    wrong_schemes.append(''.join(random.choice(string.lowercase) for i in range(length)))

wrong_authorities = []
for i in range(0, count):
    wrong_authorities.append(str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255)))

headers = {":method": ["GET", "HEAD", "POST", "PUT", "DELETE", "TRACE", "OPTIONS", "CONNECT", "PATCH", "WRONG"] + wrong_methods, ":scheme": ["http"] + wrong_schemes, ":authority": [target_ip] + wrong_authorities, ":path": "/"}
base_http2_frame.set_header_data_frame(headers, "HTTP/2 Headers and Datas")

sess.connect(sess.root, s_get("HTTP/2 Magic and Settings"), callback=None)
sess.connect(s_get("HTTP/2 Magic and Settings"), s_get("HTTP/2 Headers and Datas"), callback=check_ack_settings_frame)

sess.post_send = send_goaway_frame

sess.fuzz()








# log file analysis
from hyper.packages.hpack.hpack import Encoder, Decoder
import struct

f = open("./fuzz_log", "r")

send_lines = []
receive_lines = []
for line in f:
    if "[DEBUG] -> Packet sent :" in line:
        send_lines.append(line.strip().decode("string_escape"))
    if "[DEBUG] -> received:" in line:
        receive_lines.append(line.strip().decode("string_escape"))

        if len(receive_lines) != len(send_lines):
            print "wrong"
            break

f.close()


send_and_receive = []
index = 0
for line in send_lines:
    sss = line.split("Packet sent : ")[-1][1:-1]
    if sss[3] == "\x01":
        length = ord(sss[0])*256*256 + ord(sss[1])*256 + ord(sss[2])
        encoded_headers = sss[9:(9+length)]
        d = Decoder()
        headers = d.decode(b''.join(encoded_headers))
	
        # process with received response
        for i in range(0, len(receive_lines[index])):
            if receive_lines[index][i] == '\'':
                break

        rsss = receive_lines[index][(i+1):-1]
        rsss_header_length = ord(rsss[0])*256*256 + ord(rsss[1])*256 + ord(rsss[2])
        rsss_encoded_headers = rsss[9:(9+rsss_header_length)]

        rsss_html = ""
        if "<html>" in rsss:
            rsss_html = "<html>" + rsss.split("</html>")[0].split("<html>")[-1] + "</html>"

        rsss_time = receive_lines[index][1:20]
        rsss_time = time.strftime("%Y/%m/%d-%H:%M:%S", time.strptime(rsss_time, "%Y-%m-%d %H:%M:%S"))



        if rsss_encoded_headers == "" or rsss[3] != '\x01':
            rsss_headers = [(u":status", u"0"), (u"response", u"")]
        else:
            d = Decoder()
            rsss_headers = d.decode(b''.join(rsss_encoded_headers))


        rsss_headers.append(("fuzztime", rsss_time))
        rsss_headers.append(("responsehtml", rsss_html))

        #html = "<html>" + rsss.split("<html>")[-1].split("</html>")[0] + "</html>"

        send_and_receive.append((dict(headers), dict(rsss_headers)))


    index = index + 1

# 0 means no response or unknown response????
expected_status_codes = {
    "GET" : 200,
    "HEAD" : 200,
    "POST" : 200,
    "PUT" : 405,
    "DELETE" : 405,
    "TRACE" : 200,
    "OPTIONS" : 200,
    "CONNECT" : 0,
    "PATCH" : 405
}

expected_valid_method = {
    "GET" : True,
    "HEAD" : True,
    "POST" : True,
    "PUT" : False,
    "DELETE" : False,
    "TRACE" : True,
    "OPTIONS" : True,
    "CONNECT" : False,
    "PATCH" : False
}

expected_valid_scheme = {
    "http": True
}

expected_valid_authority = {
    target_ip: True
}




result_file_path = "./result_" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"
with open(result_file_path, 'wb') as csvfile:
    spamwriter = csv.writer(csvfile)
    #spamwriter.writerow(["No.", "time", "method", "scheme", "authority", "status code", "response html", "expected code", "consistent"])
    #spamwriter.writerow(["No.", "time", "method", "scheme", "authority", "receive headers", "status code", "response html", "expected code", "consistent"])
    spamwriter.writerow(["No.", "time", "method", "scheme", "authority", "is valid method", "is valid scheme", "is valid authority", "receive headers", "status code", "response html"])

    for i in range(0, len(send_and_receive)):
        send_headers = send_and_receive[i][0]
        receive_headers = send_and_receive[i][1]

        line = [str(i), receive_headers["fuzztime"], send_headers[":method"], send_headers[":scheme"], send_headers[":authority"]]
        html = repr(receive_headers["responsehtml"])
        del receive_headers["fuzztime"]
        del receive_headers["responsehtml"]

        """
        line = line + [repr(receive_headers), receive_headers[":status"], html]

        if send_headers[":method"] in expected_status_codes:
            line = line + [str(expected_status_codes[send_headers[":method"]])]
        else:
            # unknown method would be treated as server error
            line = line + ["501"]

        if line[-1] == line[-3]:
            line = line + ["True"]
        else:
            line = line + ["False"]
        """


        if send_headers[":method"] in expected_valid_method:
            vmethod = expected_valid_method[send_headers[":method"]]
        else:
            vmethod = False

        if send_headers[":scheme"] in expected_valid_scheme:
            vscheme = expected_valid_scheme[send_headers[":scheme"]]
        else:
            vscheme = False

        if send_headers[":authority"] in expected_valid_authority:
            vauthority = expected_valid_authority[send_headers[":authority"]]
        else:
            vauthority = False

        line = line + [repr(vmethod), repr(vscheme), repr(vauthority), repr(receive_headers), receive_headers[":status"], html]


        spamwriter.writerow(line)




