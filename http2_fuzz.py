from sulley import *
from requests import base_http2_frame

def clean_receive_buffer(sock):
    try:
        #sock.recv(4096)
        pass
    except:
        pass

def update_stream_id(session, node, edge, sock):
    try:
        #session.last_recv = sock.recv(4096)
        pass
    except:
        pass
    stream_id = 1
    #s_update("header stream id", stream_id)
    #s_update("data stream id", stream_id)

def check_ack_settings_frame(session, node, edge, sock):
    recv = session.last_recv
    if recv and recv[3] == '\x04' and recv[4] == '\x00':
        sock.send("\x00\x00\x00\x04\x01\x00\x00\x00\x00")

    return


sess = sessions.session(sleep_time = 0.0001)
target = sessions.target("192.168.144.104", 8080)
#target = sessions.target("104.131.161.90", 80)
sess.add_target(target)

headers = {":method": ["GET", "POST"], ":scheme": ["http"], ":authority": "192.168.144.104", ":path": "/"}
#headers = {":method": "GET", ":scheme": "http", ":authority": "http2bin.org", ":path": "/ip"}
base_http2_frame.set_header_frame(headers)

sess.pre_send = clean_receive_buffer
sess.connect(sess.root, s_get("HTTP/2 Magic"), callback=None)
sess.connect(s_get("HTTP/2 Magic"), s_get("HTTP/2 Settings disable push"), callback=None)



sess.connect(s_get("HTTP/2 Settings disable push"), s_get("HTTP/2 Headers"), callback=check_ack_settings_frame)
#sess.connect(s_get("HTTP/2 Settings disable push"), s_get("HTTP/2 Headers"), callback=check_ack_settings_frame)
#sess.connect(s_get("HTTP/2 Settings disable push"), s_get("HTTP/2 Settings ACK"), callback=check_ack_settings_frame)
#sess.connect(s_get("HTTP/2 Settings ACK"), s_get("HTTP/2 Headers"), callback=check_ack_settings_frame)
#sess.connect(s_get("HTTP/2 Headers"), s_get("HTTP/2 Datas"), callback=None)
sess.post_send = clean_receive_buffer

sess.fuzz()

