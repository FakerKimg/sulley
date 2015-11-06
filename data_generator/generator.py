from sulley import *
from requests.regular import *
import time
import logging

def change_line(session, node, edge, sock):
    session._file.write("\n")


def generate_regular_data(_type):
    t = time.time()
    timestr = time.strftime(_type.lower() + "%Y-%m-%d-%H-%M-%s", time.localtime(t))
    _file_path = "test_datas/" + timestr
    _file = open(_file_path, "w")

    sess = sessions.session(sleep_time = 0.0001, _file=_file, log_level=logging.ERROR)
    target = sessions.target("127.0.0.1", 80)
    sess.add_target(target)

    for name, value in blocks.REQUESTS.iteritems():
        if _type in name:
            sess.connect(sess.root, s_get(name), callback=change_line)

    #sess.connect(sess.root, s_get(request_name), callback=change_line)

    sess.fuzz()
    _file.close()

    return _file_path

