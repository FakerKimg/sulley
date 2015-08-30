from bs4 import BeautifulSoup
import requests
import random
import urlparse

class BufferOverflow():
    def __init__(self, url, detail):
        self.url = url
        self.detail = detail
        self.input_pairs = []
        self.tag_num = {}
        self.status = [0,0,0,0,0]
        self.input_tag_num = {}
        self.ask = False  #To decide whether to ask user to input payload by themself
        self.repeat = False
    
    def randomizer(self):
        str2 = ""
        str1 = "QAa0bcLdUK2eHfJgTP8XhiFj61DOklNm9nBoI5pGqYVrs3CtSuMZvwWx4yE7zR"

        for i in range(300):
            r = random.randint(0, 61)
            str2 = str2 + str1[r]

        return str2


    def parseInput(self, key=""):
        response = requests.get(self.url) # Todo: identify which to use, GET or POST ?
        print 'key:',key
        if response.status_code != 200:
            # Todo
            pass
        self.status[response.status_code/100-1] += 1
        html = response.content
        soup = BeautifulSoup(html)
        forms = soup.select("form")
        # print "forms # : " + forms.len(forms)
        test_tag = ["form", "input", "div", "section","article","main","aside","header","footer","nav","figure","figcaption","template","video","audio","embed","mark","embed","mark","progress","meter","time","ruby","rt","rp","bdi","wbr","canvas","datalist","keygen","output"]
        input_tag = ['tel','search','url','email','date','time','number','range','color','text','hidden','password','radio','checkbox','submit']
        for tag in test_tag:
            self.tag_num[tag]=len(soup.select(tag))
        for tag in input_tag:
            self.input_tag_num[tag] = 0
        
        self.input_pairs = []
        for form in forms:
            action = form.get("action", "")
            if action == "":
                continue
            #print 'action:',action,'\n'
            inputs = form.find_all("input")
            #print 'input:',inputs,'\n'
            form_content = {}
            form_content["action"] = form["action"]
            form_content["payload"] = {}
           
            #count the number of input label
            if key != '' or not self.repeat:
                for _input in inputs:
                    self.input_tag_num[_input['type'].lower()] += 1
            if key == '' and self.repeat:
                self.repeat = False
            
            for _input in inputs:
                types = _input.get("type","")
                if types == "":
                    continue
                #if "type" not in _input:
                #    continue
                payload = ""
                if self.ask:
                    print "The input's name is %s and its type is %s."%(_input["name"],_input["type"])
                    payload = raw_input("Press enter directly if you don't want to input payload by yourself.\n")
                if key != '':
                    form_content['payload'][_input["name"]] = key
                elif payload == "":
                    if _input["type"].lower() == "text" or _input["type"].lower() == "hidden" or _input["type"].lower() == "password":
                        s = self.randomizer()
                        if "value" in _input:
                            s = _input["value"] + s
                        form_content['payload'][_input["name"]] = s
                    elif _input["type"].lower() == "radio":
                        form_content['payload'][_input["name"]] = "checked"
                    elif _input["type"].lower() == "checkbox":
                        form_content['payload'][_input["name"]] = "checked"
                else:
                    form_content['payload'][_input["name"]] = payload
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

            print response

        return


    def analyzeBufferOverflow(self):
        print '###################################################################################'
        print '<---BUFFER OVERFLOW ANALYSIS--->'
        for k,v in self.tag_num.iteritems():
            print 'Total # of %s tag:%d'%(k,v)
        print '###################################################################################'
        print 'Input tag type:'
        print 'Total # of input tag:%d'%(self.tag_num['input'])
        print 'Detail:'
        for k,v in self.input_tag_num.iteritems():
            print 'Total # of %s tag in input tags:%d'%(k,v)
        print '###################################################################################'
        print '<<-Categorizing the available data on basis of HTTP Status Codes->>'
        print "Informational Codes 1xx Series:",self.status[0]
        print "Successful Client Interaction related 2xx Series:",self.status[1]
        print "Redirection related 3xx Series:",self.status[2]
        print "Client Error related 4xx Series:",self.status[3]
        print "Server Error related 5xx Series:",self.status[4]
        print '###################################################################################'


