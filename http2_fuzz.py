from sulley import *
from requests import base_http2_frame

def check_ack_settings_frame(session, node, edge, sock):
    recv = session.last_recv
    if recv and recv[3] == '\x04' and recv[4] == '\x00':
        sock.send("\x00\x00\x00\x04\x01\x00\x00\x00\x00")

    return


sess = sessions.session(sleep_time = 0.0001)
target = sessions.target("192.168.144.104", 8080)
#target = sessions.target("104.131.161.90", 80)
sess.add_target(target)

headers = {":method": ["GET", "POST", "PUT", "DELETE"], ":scheme": ["http", "ftp"], ":authority": "192.168.144.104", ":path": "/"}
#headers = {":method": "GET", ":scheme": "http", ":authority": "http2bin.org", ":path": "/ip"}
base_http2_frame.set_header_data_frame(headers, "HTTP/2 Headers and Datas")

sess.connect(sess.root, s_get("HTTP/2 Magic"), callback=None)
sess.connect(s_get("HTTP/2 Magic"), s_get("HTTP/2 Settings disable push"), callback=None)
sess.connect(s_get("HTTP/2 Settings disable push"), s_get("HTTP/2 Headers and Datas"), callback=check_ack_settings_frame)

sess.fuzz()

