from sulley import *
from utils.html_parser import *
from requests.form_post import form_post_requests


class print_session(sessions.session):
    def post_send(self, sock):
        print self.last_recv


html_url = "http://www.hhserver.com/test.html"
html = get_html(html_url)
parser = HtmlParser(html)
forms = parser.find_inputs_in_forms()

datas = {
    "default": "/home/swpotato/dcns/fuzzdb/attack-payloads/sql-injection/payloads-sql-blind/payloads-sql-blind-MySQL-WHERE.txt",
}

form_post_requests(forms, datas)

#sess = sessions.session(sleep_time = 0.0001)
sess = print_session(sleep_time = 0.0001)
target = sessions.target("192.168.144.104", 80)
sess.add_target(target)

form_count = 0
for form in forms:
    sess.connect(sess.root, s_get("HTTP VERBS POST" + str(form_count)))
    form_count = form_count + 1


sess.fuzz()


