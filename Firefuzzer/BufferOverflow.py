from bs4 import BeautifulSoup
import requests
import random
import urlparse

class BufferOverflow():
    def __init__(self, url, detail):
        self.url = url
        self.detail = detail
        self.input_pairs = []

    def randomizer(self):
        str2 = ""
        str1 = "QAa0bcLdUK2eHfJgTP8XhiFj61DOklNm9nBoI5pGqYVrs3CtSuMZvwWx4yE7zR"

        for i in range(300):
            r = random.randint(0, 61)
            str2 = str2 + str1[r]

        return str2


    def parseInput(self):
        response = requests.get(self.url) # Todo: identify which to use, GET or POST ?
        if response.status_code != 200:
            # Todo
            pass

        html = response.content
        soup = BeautifulSoup(html)
        forms = soup.select("form")
        # print "forms # : " + forms.len(forms)


        self.input_pairs = []
        for form in forms:
            action = form.get("action", "")
            if action == "":
                continue

            inputs = form.find_all("input")

            form_content = {}
            form_content["action"] = form["action"]
            form_content["payload"] = {}

            for _input in inputs:
                if "type" not in _input:
                    continue
                elif _input["type"].lower() == "text" or _input["type"].lower() == "hidden" or _input["type"].lower() == "password":
                    s = self.randomizer()
                    if "value" in _input:
                        s = _input["value"] + s
                    form_content[_input["name"]] = s
                elif _input["type"].lower() == "radio":
                    form_content[_input["name"]] = "checked"
                elif _input["type"].lower() == "checkbox":
                    form_content[_input["name"]] = "checked"

            self.input_pairs.append(form_content)

        print self.input_pairs

        self.sendBack()
        return

    def sendBack(self):
        for form in self.input_pairs:
            if not form["action"].startswith("http"): 
                urlinfo = urlparse.urlparse(self.url)
                #print urlinfo,'1',form['action']   
                url = urlinfo.scheme + '://' + urlinfo.netloc + '/' + form["action"]
            else:
                url = form["action"]
            
            #print 'payload:',form['payload']
           
            response = requests.post(url, data = form['payload'])
            if response.status_code != 200:
                # Todo
                pass

            #print response.content

        return


    def analyzeBufferOverflow(self):
        pass




