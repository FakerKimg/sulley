from sulley import *
from utils.html_parser import *
from requests.form_post import form_post_requests
import logging

class print_session(sessions.session):
    def post_send(self, sock):
        print self.last_recv


html_url = "http://www.hhserver.com/Test.html"
html = get_html(html_url)
parser = HtmlParser(html)
forms = parser.find_inputs_in_forms()

datas = {
    #"default": "/home/swpotato/dcns/fuzzdb/attack-payloads/sql-injection/payloads-sql-blind/payloads-sql-blind-MySQL-WHERE.txt",
    "tel": "/home/swpotato/dcns/sulley/test_datas/tel",
    #"color": "/home/swpotato/dcns/sulley/test_datas/color",
    #"date": "/home/swpotato/dcns/sulley/test_datas/date",
    #"email": "/home/swpotato/dcns/sulley/test_datas/email",
    #"number": "/home/swpotato/dcns/sulley/test_datas/number",
    #"password": "/home/swpotato/dcns/sulley/test_datas/password",
    #"range": "/home/swpotato/dcns/sulley/test_datas/range",
    #"text": "/home/swpotato/dcns/sulley/test_datas/text",
    #"time": "/home/swpotato/dcns/sulley/test_datas/time",
    #"url": "/home/swpotato/dcns/sulley/test_datas/url",
}

form_post_requests(forms, datas)

#sess = sessions.session(sleep_time = 0.0001)
sess = print_session(sleep_time = 0.0001, logfile = "/home/swpotato/dcns/sulley/tel_log_file", log_level = logging.DEBUG, logfile_level = logging.DEBUG)
target = sessions.target("192.168.144.104", 80)
sess.add_target(target)

form_count = 0
for form in forms:
    sess.connect(sess.root, s_get("HTTP VERBS POST" + str(form_count)))
    form_count = form_count + 1


sess.fuzz()


