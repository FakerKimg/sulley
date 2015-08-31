from bs4 import BeautifulSoup
import urlparse
import urllib2

def get_html(url):
    response = urllib2.urlopen(url)
    return response.read()


class HtmlParser():
    def __init__(self, html = None):
        self.html = html

    def set_html(self, html):
        self.html = html

    def get_html(self):
        return self.html

    def find_inputs_in_forms(self):
        assert self.html, "no given html"
        soup = BeautifulSoup(self.html)
        inputs_form = []

        forms = soup.select("form")
        for form in forms:
            action = form.get("action", "")
            if action == "":
                continue

            '''
            if not action.startswith("http"):
                urlinfo = urlparse.urlparse(html_url)
                action = urlinfo.scheme + "://" + urlinfo.netloc + action
            '''
            if not action.startswith("/"):
                action = '/' + action

            form_content = {}
            form_content["action"] = action
            form_content["inputs"] = []

            inputs = form.find_all("input")
            for _input in inputs:
                t = _input.get("type", "")
                n = _input.get("name", "")
                v = _input.get("value", "")

                form_content["inputs"].append({"type": t, "name": n, "value": v})

            inputs_form.append(form_content)

        return inputs_form

