from bs4 import BeautifulSoup
import requests
import random
import urlparse
import re
import time
import csv
import os
import difflib as diff

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
        self.payload_count = 0
        self.folder = ''

    def set_folder(self,s):
        self.folder = s

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
            for line in fin:
                self.payload[filename].append(line[:-1])
        else:
            for f in self.input_file:
                if f.startswith(filename):
                    fin = open(path+f,'r')
                    for line in fin:
                        self.payload[filename].append(line[:-1])
	
    def similar(self,a,b):
        sim = [0.0,[],[]]
        for i in range(len(a)):
            c_a = a[i].split()
            c_b = b[i].split()
            #s = diff.SequenceMatcher(None,c_a,c_b)
            d = diff.Differ()
            result = list(d.compare(c_a,c_b))
            #print result
            com = []
            different = 0.0
            total_len = 0.0
            for k in result:
                if k[0] == '?':
                    continue
                total_len += len(k)-2
                if k[0]!= ' ':
                    com.append(k)
                    different += len(k)-2
            #print s.ratio(),same/total_len
            if total_len!=0:
                sim[1].append(1-different/total_len)
            else:
                sim[1].append(1)
            sim[2].append(com)
        sim[0] = sum(sim[1])/len(a)
        return sim
		
    def test_input(self,sleep_time):
        if len(self.input_pairs)==0:
            return
        t0 = time.time()
        url = self.url[7:].replace('.','_').replace('/','_')
        if not os.path.exists('./output/'+self.folder+'/'+url):
            os.makedirs('./output/'+self.folder+'/'+url)
        self.input_file = os.listdir('./testcase/')
        self.input_type = ['text','password','tel','email','url','date','time','number','range','color']
        for k in range(len(self.input_type)):
            self.payload[self.input_type[k]] = []
            self.read_payload(self.input_type[k],'./testcase/',False)
        self.writer.append(csv.writer(open('./output/'+self.folder+'/'+url+'/'+'summary.csv','w')))
        self.writer[len(self.writer)-1].writerow(('Form','Payload','Status code','Request time','Response time','Response','Response body','Average correct rate','Correct rate','Diff'))
        payload_count = []
        self.correct = {}
        self.correct['text'] = '12abAB'
        self.correct['password'] = '12abAB'
        self.correct['tel'] = '0911111111'
        self.correct['email'] = 'test@gmail.com.tw'
        self.correct['url'] = 'http://www.google.com'
        self.correct['week'] = '2015-11'
        self.correct['month'] = '2015-11'
        self.correct['date'] = '2015 11 08'
        self.correct['datetime'] = '2015 11 08'
        self.correct['datetime-local'] = '2015 11 08'
        self.correct['number'] = '1'
        self.correct['range'] = '0'
        self.correct['color'] = '#ffffff'
        self.correct['time'] = '12:00'
        
        for pairs in self.input_pairs:
            for _input in pairs['input']:
                if _input['type'] not in self.correct:
                    s = self.randomizer()
                    if "value" in _input:
                        s = _input["value"] + s
                    pairs['payload'][_input['name']]=s
                    continue
                pairs['payload'][_input['name']] = self.correct[_input['type']]
        self.correct['response'] = self.sendBack()
        if type(self.correct['response'])!=list:
            print 'Unable to fuzz the target website'
            print 'The status_code of request is',self.correct['response']
            self.status[self.correct['response']/100-1] -= 1
            return ;
        else:
            for k in range(len(self.correct['response'])):
                self.status[self.correct['response'][k].status_code/100-1]-=1
                self.correct['response'][k] = re.split('\n+',BeautifulSoup(self.correct['response'][k].text).text.strip())
        #print pairs['payload']
        #print self.correct['response'][0].text 

        for k in self.input_type:
            payload_count.append(len(self.payload[k]))
        self.payload_count = min(payload_count)
        for i in range(self.payload_count):
            for pairs in self.input_pairs:
                for _input in pairs['input']:
                    if _input['type'] not in self.input_type:
                        s = self.randomizer()
                        if "value" in _input:
                            s = _input["value"] + s
                        pairs['payload'][_input['name']]=s
                        continue
                    pairs['payload'][_input['name']]=self.payload[_input['type']][i] 
                print pairs['payload']
            t1 = time.time()
            response = self.sendBack()
            t2 = time.time()
            #print response
            if type(response)!=list:
                self.writer[len(self.writer)-1].writerow(('none',self.input_pairs[0]['payload'],response,t1-t0,t2-t0,'none','none','none','none','none'))
            else:
                for k in range(len(response)):
                    res = re.split('\n+',BeautifulSoup(response[k].text).text.strip())
                    if len(res)==len(self.correct['response'][k]):
                        similarity = self.similar(self.correct['response'][k],res)
                    else:
                        cres = ' '.join(self.correct['response'][k])
                        similarity = self.similar([cres],[' '.join(res)])
                    #print similarity
                    res = '\n'.join(res)
                    self.writer[len(self.writer)-1].writerow((k,self.input_pairs[k]['payload'],response[k].status_code,t1-t0,t2-t0,response[k].text.encode('utf-8'),res.encode('utf-8'),similarity[0],similarity[1],similarity[2]))
                    #self.writer[len(self.writer)-1].writerow((k,self.input_pairs[k]['payload'],response[k].status_code,t1-t0,t2-t0))
            time.sleep(sleep_time)
        
    def parse_html(self):
        response = requests.get(self.url) 
        html = response.content
        soup = BeautifulSoup(html)
        forms = soup.select("form")
        # print "forms # : " + forms.len(forms)
        test_tag = ["form", "input", "div", "section","article","main","aside","header","footer","nav","figure","figcaption","template","video","audio","embed","mark","embed","mark","progress","meter","time","ruby","rt","rp","bdi","wbr","canvas","datalist","keygen","output"]
        html4_tag = ['text','password','radio','checkbox','submit','button','file','hidden','image','reset']
        html5_tag = ['color','date','datetime','datetime-local','email','month','number','range','search','tel','time','url','week']
        for tag in test_tag:
            self.tag_num[tag]=len(soup.select(tag))
        for tag in html4_tag:
            self.input_tag_num[tag] = 0
        for tag in html5_tag:
            self.input_tag_num[tag] = 0
	self.input_pairs = []
        for form in forms:
            html4 = 0
            html5 = 0
            action = form.get("action", "")
            method = form.get("method","").lower()
            print action
            #print 'method:',method
            if action == "" or not (method == "post" or method == "get") :
                continue
            #print 'action:',action,'\n'
            inputs = form.find_all("input")
            print 'input:',inputs,'\n'
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
                if t == '':
                    continue
                n = _input.get("name","")
                v = _input.get("value","")
		form_content["input"].append({'type':t,'name':n,'value':v})
		self.input_tag_num[_input['type'].lower()] += 1
                if t in html4_tag:
                    html4 += 1
                else:
                    html5 += 1
            print 'HTML4 input count:',html4
            print 'HTML5 input count:',html5
            self.input_pairs.append(form_content)
        print self.input_pairs
		
		
    def sendBack(self,out = False,i=0):
        outcome = []
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
            else:
                response = requests.get(url, data = self.input_pairs[k]['payload'])
            outcome.append(response)
            self.status[response.status_code/100-1] += 1
            print response
            if response.status_code != 200:
                return response.status_code
            if out:
                res = re.split('\n+',BeautifulSoup(response.text).text.strip())
                res = '\n'.join(res)
                self.writer[len(self.writer)-1].writerow((k,self.input_pairs[k]['payload'],response.status_code,response.text,res))
        return outcome

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


