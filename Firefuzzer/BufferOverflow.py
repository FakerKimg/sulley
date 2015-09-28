from bs4 import BeautifulSoup
import requests
import random
import urlparse
import re
import time

class BufferOverflow():
    def __init__(self, url):
        self.url = url
        self.input_pairs = []
        self.tag_num = {}
        self.status = [0,0,0,0,0]
        self.input_tag_num = {}
        self.ask = False  #To decide whether to ask user to input payload by themself
        self.payload = {} 
        self.writer = []

    def randomizer(self):
        str2 = ""
        str1 = "QAa0bcLdUK2eHfJgTP8XhiFj61DOklNm9nBoI5pGqYVrs3CtSuMZvwWx4yE7zR"

        for i in range(300):
            r = random.randint(0, 61)
            str2 = str2 + str1[r]

        return str2

    def read_payload(self,filename,path):
        fin = open(path,'r')
        #fin.readline() # the first line
        while 1:
            tmp = fin.readline()
            if tmp == "":
                break
            self.payload[filename].append(tmp[:-1])
            '''
            if tmp[:2] == '0x':
                self.payload.append(int(tmp[2:-1],16))
            else:
                self.payload.append(int(tmp[:-1]))
            '''
			
    def autotest(self,sleep_time):
        #self.filelist = ['payloads-sql-blind-MSSQL-INSERT.txt','payloads-sql-blind-MSSQL-WHERE.txt','payloads-sql-blind-MySQL-INSERT.txt','payloads-sql-blind-MySQL-ORDER_BY.txt','payloads-sql-blind-MySQL-WHERE.txt']
        self.filelist = ['integer-overflows.txt']

        for f in self.filelist:
            self.payload[f] = []
            self.read_payload(f,'./attack-payloads/'+f)
            print '###################################################################################'
            print 'Test file:%s'%(f)			
            for s in self.payload[f]:
                self.parseInput(s)
                time.sleep(sleep_time)	        
    
    def test_input(self,sleep_time):
       input_type = ['text','password','tel','email','url','date','time','number','range','color']
       for k in input_type:
           self.payload[k] = []
           self.read_payload(k,'./input_type/'+k)
           self.writer.append(open('./input_type/'+k+'_result','w'))  
       for i in range(40):
           for pairs in self.input_pairs:
               for _input in pairs['input']:
                   if _input['type'] not in input_type:
                       continue
                   self.writer[input_type.index(_input['type'])].write(self.payload[_input['type']][i]+'\n')
                   pairs['payload'][_input['name']]=self.payload[_input['type']][i] 
               print pairs['payload']
               self.sendBack(True)
               time.sleep(sleep_time)
 
        
    def parse_html(self,key = ''):
        response = requests.get(self.url) # Todo: identify which to use, GET or POST ?
        #print 'key:',key
        if response.status_code != 200:
            # Todo 
            pass
        #self.status[response.status_code/100-1] += 1
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
	    form_content["input"] = []
           
            #count the number of input label
            for _input in inputs:
	        types = _input.get("type","")
		if type == "":
		    continue
                t = _input.get("type","")
                n = _input.get("name","")
                v = _input.get("value","")
		form_content["input"].append({'type':t,'name':n,'value':v})
		self.input_tag_num[_input['type'].lower()] += 1
            self.input_pairs.append(form_content)
        print self.input_pairs
		
		
    def parseInput(self, key=""):
	for pairs in self.input_pairs:
 	    for _input in pairs['input']:
                payload = ""
                if self.ask:
                    print "The input's name is %s and its type is %s."%(_input["name"],_input["type"])
                    payload = raw_input("Press enter directly if you don't want to input payload by yourself.\n")
                if key != '':
                    pairs['payload'][_input["name"]] = key
                elif payload == "":
                    if _input["type"].lower() == "text" or _input["type"].lower() == "hidden" or _input["type"].lower() == "password":
                        s = self.randomizer()
                        if "value" in _input:
                            s = _input["value"] + s
                        pairs['payload'][_input["name"]] = s
                    elif _input["type"].lower() == "radio":
                        pairs['payload'][_input["name"]] = "checked"
                    elif _input["type"].lower() == "checkbox":
                        pairs['payload'][_input["name"]] = "checked"
                else:
                    pairs['payload'][_input["name"]] = payload
            print pairs['payload']
            self.sendBack()

    def sendBack(self,out = False):
        for form in self.input_pairs:
            if not form["action"].startswith("http"): 
                urlinfo = urlparse.urlparse(self.url)
                #print urlinfo,'1',form['action']   
                url = urlinfo.scheme + '://' + urlinfo.netloc + '/' + form["action"]
            else:
                url = form["action"]
            
            #print 'payload:',form['payload']
           
            response = requests.post(url, data = form['payload'])
            self.status[response.status_code/100-1] += 1
            if response.status_code != 200:
                # Todo
                pass
            print response
            if out:
                res = BeautifulSoup(response.text)
                res = re.split('\n+',res.text.strip())
                for k in range(len(res)):
                    self.writer[k].write(res[k]+'\n')
            #print response.text.replace('<br>','\n')


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


