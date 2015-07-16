from sulley import *
from utils.html_parser import *

def recv_bad_request(sock):
    sock.recv(4096)


html_url = "http://www.hhserver.com/test.html"
html = get_html(html_url)
parser = HtmlParser(html)
inputs_form = parser.find_inputs_in_forms()


# form_post.py use inputs_form directly
from requests.form_post import form_post_requests
form_post_requests(inputs_form)

sess = sessions.session()
sess.post_send = recv_bad_request
target = sessions.target("192.168.144.104", 80)
sess.add_target(target)

count = 0
for form in inputs_form:
    sess.connect(sess.root, s_get("HTTP VERBS POST" + str(count)))
    count = count + 1

sess.fuzz()




