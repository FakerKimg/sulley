from bs4 import BeautifulSoup
import requests
import random
import urlparse
import re
import time
import csv
import os
from hyper import HTTP20Connection
from urlparse import urlparse

class BufferOverflow():
    def __init__(self, url):
        self.url = url
        self.input_pairs = []
        self.tag_num = {}
        self.status = [0,0,0,0,0]
        self.input_tag_num = {}
        self.ask = False  #To decide whether to ask user to input payload by themself
        self.oursite = True #To decide whether to decode the respose site from php or not, but we only can decode the testing site made by ourself.
        self.payload = {} 
        self.writer = []

    def randomizer(self):
        str2 = ""
        str1 = "QAa0bcLdUK2eHfJgTP8XhiFj61DOklNm9nBoI5pGqYVrs3CtSuMZvwWx4yE7zR"

        for i in range(300):
            r = random.randint(0, 61)
            str2 = str2 + str1[r]

        return str2

    def read_payload(self,filename,path,path_correct):
        if path_correct:
            fin = open(path,'r')
            #fin.readline() # the first line
            for line in fin:
                self.payload[filename].append(line[:-1])
        else:
            for f in self.input_file:
                if f.startswith(filename):
                    fin = open(path+f,'r')
                    for line in fin:
                        self.payload[filename].append(line[:-1])
			
    def autotest(self,sleep_time):
        self.filelist = ['payloads-sql-blind-MSSQL-INSERT.txt','payloads-sql-blind-MSSQL-WHERE.txt','payloads-sql-blind-MySQL-INSERT.txt','payloads-sql-blind-MySQL-ORDER_BY.txt','payloads-sql-blind-MySQL-WHERE.txt']
        #self.filelist = ['integer-overflows.txt']
        self.input_type = ['text','password','tel','email','url','date','time','number','range','color']
        url = self.url[7:].replace('.','_').replace('/','_')
        self.oursite = False
        self.writer.append(csv.writer(open('./output/'+url+'/'+'summary.csv','w'))) 
        for f in self.filelist:
            self.payload[f] = []
            self.read_payload(f,'./attack-payloads/'+f,True)
            print '###################################################################################'
            print 'Test file:%s'%(f)			
            for s in self.payload[f]:
                self.parseInput(key = s,out = True)
                time.sleep(sleep_time)	        
    
    def test_input(self,sleep_time):
       url = self.url[7:].replace('.','_').replace('/','_')
       if not os.path.exists('./output/'+url):
           os.makedirs('./output/'+url)
       self.input_file = os.listdir('./input_type/')
       self.input_type = ['text','password','tel','email','url','date','time','number','range','color']
       for k in range(len(self.input_type)):
           self.payload[self.input_type[k]] = []
           self.read_payload(self.input_type[k],'./input_type/',False)
           if self.oursite:
               self.writer.append(csv.writer(open('./output/'+url+'/'+self.input_type[k]+'_result.csv','w')))
               self.writer[k].writerow(('Form','Input','Output'))
       self.writer.append(csv.writer(open('./output/'+url+'/'+'summary.csv','w')))
       self.writer[len(self.writer)-1].writerow(('Form','Payload','Status code','Response'))
       payload_count = []
       for k in self.input_type:
           payload_count.append(len(self.payload[k]))
       for pairs in self.input_pairs:
           for i in range(min(payload_count)):
               for _input in pairs['input']:
                   if _input['type'] not in self.input_type:
                       continue
                   #self.writer[input_type.index(_input['type'])].write(self.payload[_input['type']][i]+'\n')
                   pairs['payload'][_input['name']]=self.payload[_input['type']][i] 
               print pairs['payload']
               self.sendBack(True,i)
               time.sleep(sleep_time)
 
        
    def parse_html(self,key = ''):
        response = requests.get(self.url) # Todo: identify which to use, GET or POST ?
        """
        HTTP2.0:
        urlinfo = urlparse(self.url)
        conn = HTTP20Connection(urlinfo.netloc)
        conn.request('GET', urlinfo.path)
        response = conn.get_response()
        """
        #print 'key:',key
        #HTTP2.0: if response.status != 200:
        if response.status_code != 200:
            # Todo 
            pass
        #self.status[response.status_code/100-1] += 1
        #HTTP2.0: html = response.read()
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
            method = form.get("method","").lower()
            print 'method:',method
            if action == "" or not (method == "post" or method == "get") :
                continue
            #print 'action:',action,'\n'
            inputs = form.find_all("input")
            #print 'input:',inputs,'\n'
            form_content = {}
            form_content["action"] = form["action"]
            form_content["payload"] = {}
	    form_content["input"] = []
            form_content["method"] = form["method"]
           
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
		
		
    def parseInput(self, key="",out = False):
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
            self.sendBack(out = out)

    def sendBack(self,out = False,i=0):
        for k in range(len(self.input_pairs)):
            if not self.input_pairs[k]["action"].startswith("http"): 
                urlinfo = urlparse.urlparse(self.url)
                #print urlinfo,'1',form['action']   
                url = urlinfo.scheme + '://' + urlinfo.netloc + '/' + self.input_pairs[k]["action"]
            else:
                url = self.input_pairs[k]["action"]
            
            #print 'payload:',form['payload']
            if self.input_pairs[k]["method"] == "post":
                response = requests.post(url, data = self.input_pairs[k]['payload'])
                """
                HTTP2.0:
                urlinfo = urlparse("url")
                conn = HTTP20Connection(urlinfo.netloc)
                body = ""
                for key, value in self.input_pairs[k]['payload'].iteritems():
                    body = body + key + '=' + value + '&'
                body = body[:-1]
                conn.request('POST', urlinfo.path, body=body)
                response = conn.get_response()
                """
            else:
                response = requests.get(url, data = self.input_pairs[k]['payload'])
                """
                HTTP2.0:
                urlinfo = urlparse("url")
                conn = HTTP20Connection(urlinfo.netloc)
                body = ""
                for key, value in self.input_pairs[k]['payload'].iteritems():
                    body = body + key + '=' + value + '&'
                body = body[:-1]
                conn.request('GET', urlinfo.path, body=body)
                response = conn.get_response()
                """
            # HTTP2.0: self.status[response.status/100-1] += 1
            self.status[response.status_code/100-1] += 1
            # HTTP2.0: print response.status
            print response
            # HTTP2.0: if response.status != 200
            if response.status_code != 200:
                # Todo
                pass
            if out:
                # HTTP2.0: content = response.read()
                # HTTP2.0: self.writer[len(self.writer)-1].writerow((k,self.input_pairs[k]['payload'],response.status, content))
                self.writer[len(self.writer)-1].writerow((k,self.input_pairs[k]['payload'],response.status_code,response.text))
                if self.oursite:
                    # res = BeautifulSoup(content)
                    res = BeautifulSoup(response.text)
                    res = re.split('\n+',res.text.strip())
                    for s in range(len(res)):
                        self.writer[s].writerow((k,self.payload[self.input_type[s]][i],res[s]))
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


