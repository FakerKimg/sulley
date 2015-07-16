from sulley import *
from requests import http

def init_message(sock):
    init = "GET /index.html HTML/1.1\r\n\r\n"



sess = sessions.session()
target_ip = "192.168.144.104"
target = sessions.target(target_ip, 80)

"""
target.netmon = pedrpc.client(target_ip,  26001)
target.procmon = pedrpc.client(target_ip,  26002)
target.vmcontrol = pedrpc.client("127.0.0.1", 26003)

target.procmon_options = {
    "proc_name": "",
    "stop_commands": [],
    "start_commands": [],
}
"""


sess.add_target(target)

sess.pre_send = init_message
sess.connect(s_get("HTTP VERBS"))
sess.connect(s_get("HTTP VERBS POST"))
sess.connect(s_get("HTTP HEADERS"))
sess.connect(s_get("HTTP COOKIE"))

'''
ref = "https://www.youtube.com/watch?v=6sooEScW07Y"
sess.pre_send = init_message
sess.connect(sess.root, s_get("HTTP"))
'''

sess.fuzz()


