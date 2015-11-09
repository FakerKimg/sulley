from sulley import *
from utils.html_parser import *
from requests import base_http2_frame

def clean_receive_buffer(sock):
    try:
        #sock.recv(4096)
        pass
    except:
        pass

def update_stream_id(session, node, edge, sock):
    try:
        #sock.recv(4096)
        pass
    except:
        pass
    stream_id = 1
    #s_update("header stream id", stream_id)
    #s_update("data stream id", stream_id)


sess = sessions.session(sleep_time = 0.0001)
target = sessions.target("192.168.144.104", 8080)
#target = sessions.target("104.131.161.90", 80)
sess.add_target(target)

headers = {":method": ["GET", "POST"], ":scheme": ["http"], ":path": "/Test1.html", "asdf": "asdf"}
#headers = {":method": "GET", ":scheme": "http", ":authority": "http2bin.org", ":path": "/ip", "asdf": "asdf"}
base_http2_frame.set_header_frame(headers)

sess.pre_send = clean_receive_buffer
sess.connect(sess.root, s_get("HTTP/2 Magic"), callback=None)
sess.connect(s_get("HTTP/2 Magic"), s_get("HTTP/2 Settings disable push"), callback=None)
sess.connect(s_get("HTTP/2 Settings disable push"), s_get("HTTP/2 Settings ACK"), callback=update_stream_id)
sess.connect(s_get("HTTP/2 Settings ACK"), s_get("HTTP/2 Headers"), callback=None)
sess.connect(s_get("HTTP/2 Headers"), s_get("HTTP/2 Datas"), callback=None)
sess.post_send = clean_receive_buffer

sess.fuzz()

