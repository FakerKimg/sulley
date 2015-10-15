from sulley import *
from requests.regular import regular_datas
import time
import logging

def change_line(session, node, edge, sock):
    session._file.write("\n")


def generate_regular_data(_type, request_name):
    t = time.time()
    timestr = time.strftime(_type + "%Y-%m-%d-%H-%M-%s", time.localtime(t))
    _file_path = "test_datas/" + timestr
    _file = open(_file_path, "w")

    sess = sessions.session(sleep_time = 0.0001, _file=_file, log_level=logging.ERROR)
    target = sessions.target("127.0.0.1", 80)
    sess.add_target(target)

    sess.connect(sess.root, s_get(request_name), callback=change_line)

    sess.fuzz()
    _file.close()

    return _file_path

