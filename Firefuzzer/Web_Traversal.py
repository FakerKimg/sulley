import urllib2
import Queue
import sys
import re
from bs4 import BeautifulSoup

QUE = Queue.Queue()
URLs = dict()

def main():
    # Check the number of arguments.
    if len(sys.argv)<2:
        print 'You have to enter the url!!'
        return
    elif len(sys.argv)>2:
        print 'You have entered too much arguments!!:'
        return
    else:
        origin_url = sys.argv[1]
        if not origin_url.startswith('http://'):
            origin_url = 'http://' + origin_url
    
    DOMAIN = ''
    DOMAIN1 = ''
    # Judge whether the root url is ended with '/' or not.
    if  origin_url[len(origin_url)-1]=='/':
        origin_url = origin_url[0:len(origin_url)-1]
    if origin_url.count('/') <= 2:
        DOMAIN = origin_url
    else:
        index = origin_url.rindex('/')
        DOMAIN1 = origin_url[0:index]

    # Try to check which domain is valid and take is as the root_url
    if len(DOMAIN)>0:
        response = get_url_content(DOMAIN)
        if not response:
            print "Root URL Error!\n"
            return
        else:
            root_url = DOMAIN
    else:
        response = get_url_content(DOMAIN1)
        if not response:
            # DOMAIN1 is invalid and try origin_url
            response = get_url_content(origin_url)
            if not response:
                print 'Root URL Error!\n'
                return
            else:
                root_url = origin_url
        else:
            root_url = DOMAIN1

    # Succeed to access to root url and get href.
    get_href(root_url,root_url,response)
    # Try to get url content based on the new urls we found.
    while not QUE.empty():
        target_url = QUE.get()
        response = get_url_content(target_url)
        if not response:
            # Failed to access to the target url.
            URLs[target_url]='Invalid'
        else:
            # Succeed to access to the target url and set it to be a valid url, and then try to get href.
            URLs[target_url] = 'Valid'
            get_href(target_url,root_url,response)
    print 'Length of all URLs:  ' + str(len(URLs))
    f = open('Web_Traversal_Result.txt','w')
    fout = open('Web_Traversal_link','w')
    fout.write(origin_url+'\n')
    f.write('Root URL = '+root_url+'\n')
    f.write('URL found : '+str(len(URLs))+'\n')
    for k,v in URLs.items():
        s = '%-100s %-10s' % (k,v)
        f.write(s+'\n')
        if v == 'valid':
            fout.write(k+'\n')
    f.close()
    fout.close()

def get_url_content(url):
    try:
        content = urllib2.urlopen(url)
        return content
    except:
        return False

def get_href(url,root,response):
    soup = BeautifulSoup(response)
    for i in soup.findAll('a'):
        temp = str(i.get('href'))
        length = len(temp)
        if length <5:
            continue
        if temp[0]=='/':
            temp = temp[1:length-1]
            length = len(temp)
        if length-1>=0:
            if temp[length-1]=='/':
                temp = temp[0:length-1]
        if 'None' in temp or len(temp)<2:
            continue
        if re.search('\?C=[A-Z]{1};O=[A-Z]{1}',temp):
            continue
        if 'http' in temp:
            if root in temp:
               complete_url = temp
            else:
               continue
        else:
            if url[len(url)-1]=='/':
                url = url[0:len(url)-1]
            if temp[0]=='/':
                temp = temp[1:len(temp)]
            complete_url = url + '/'+ temp
        if complete_url not in URLs:
            URLs[complete_url] = 'Not determined'
            QUE.put(complete_url)

if __name__ == '__main__':
    main()
