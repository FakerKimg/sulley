import urllib2
import Queue
import sys
import re
from bs4 import BeautifulSoup

QUE = Queue.Queue()
URLs = dict()

# Set the following flags to True if you want to filter them out.
FLAGS = {
        'AUDIO' : True,
        'PDF' : True,
        'VIDEO': True,
        'IMAGE' : True,
        'ARCHIVE' : True }

# File extension in the list will be filtered out.
Audio_Filter = ['.mp3', '.flac', '.wma']
Video_Filter = ['.mp4', '.m4p', '.m4v', '.mkv', '.flv', '.vob', '.gif', '.avi', '.mov', '.wmv', '.mpg', '.mpeg', '.3gp']
Image_Filter = ['.jpg', '.jpeg', '.gif', '.bmp', '.png', '.tiff']
Archive_Filter = ['.iso', '.tar', '.bz2', '.gz', '.7z', '.s7z', '.dmg', '.jar', '.rar', '.tar.gz', '.tgz', '.tar.bz2', '.zoo', '.zip' ]

def main():
    # Check the number of arguments.
    if len(sys.argv)<2:
        print 'You have to input the url!!'
        return
    elif len(sys.argv)>2:
        print 'You have inputted too much arguments!!:'
        return
    else:
        origin_url = sys.argv[1]

    root_url = origin_url

    if root_url[len(root_url)-1]!='/':
        root_url = root_url+'/'

    response = get_url_content(root_url)
    if not response:
        print 'Root URL Error!\n'
        return
    
    # Succeed to access to root url and then try to get href in root url.
    # If any href founded, it will be put into QUE.   
    get_href(root_url,root_url,response)

    # Try to get url content based on the new urls we found.
    count_valid = 0
    count_invalid = 0
    
    while not QUE.empty():
        target_url = QUE.get()
        print target_url
        response = get_url_content(target_url)
        if not response:
            # Failed to access to the target url.
            URLs[target_url]='Invalid'
            count_invalid += 1
        else:
            # Succeed to access to the target url and set it to be a valid url, and then try to get href.
            URLs[target_url] = 'Valid'
            count_valid += 1
            get_href(response.geturl(),root_url,response)

    # Traverse completed. Write the results in to file.
    print 'Length of all URLs:  ' + str(len(URLs))
    f1 = open('Web_Traversal_Result_ALL.txt','w+')
    f2 = open('Web_Traversal_Result_VALID.txt','w+')
    f3 = open('Web_Traversal_Result_INVALID.txt','w+')
    fout = open('Web_Traversal_link','w')
    f1.write('Root URL = '+root_url+'\n')
    f2.write('Root URL = '+root_url+'\n')
    f3.write('Root URL = '+root_url+'\n')
    f1.write('URL found : '+str(len(URLs))+'\n')
    f1.write('Number of Valid URLs : ' + str(count_valid)+'\n')
    f2.write('Number of Valid URLs : ' + str(count_valid)+'\n')
    f1.write('Number of Invalid URLs : ' + str(count_invalid)+'\n')
    f3.write('Number of Invalid URLs : ' + str(count_invalid)+'\n')
    fout.write(origin_url+'\n')
    for k,v in URLs.items():
        s = '%-100s %-10s' % (k,v)
        f1.write(s+'\n')
        if v == 'Valid':
            f2.write(s+'\n')
            fout.write(k+'\n')
        if v == 'Invalid':
            f3.write(s+'\n')
    f1.close()
    f2.close()
    f3.close()
    fout.close()

def get_url_content(url):
    try:
        content = urllib2.urlopen(url)
        return content
    except:
        return False

def get_href(url,root,response):
    soup = BeautifulSoup(response)
    for tag_a in soup.findAll('a'):
        # Remember to reset these flags.
        FLAG_Current_Folder = False
        FLAG_HREF_HAS_HTTP = False
        FLAG_IMAGE_FOUND = False
        FLAG_AUDIO_FOUND = False
        FLAG_VIDEO_FOUND = False
        FLAG_ARCHIVE_FOUND = False
        FLAG_PDF_FOUND = False
        GO_BACK = 0
        
        # Get url link in 'href'.
        try:
            href = str(tag_a.get('href'))
        except:
            href = str(tag_a.get('href').encode('utf-8'))

        complete_url = ''

        if len(href) < 4:
            continue

        # Deal with absolute url
        elif ('http://' in href) or ('https://' in href):
            if href.find(root)==0:
                complete_url = href
                FLAG_HREF_HAS_HTTP = True
            else:
               continue

        # Deal with special cases in href.
        elif ('None' in href) or len(href)<2:
            continue
        elif re.search('\?C=[A-Z]{1};O=[A-Z]{1}',href):
            continue
        elif href[0]=='#' or ('javascript' in href) or ('mailto:' in href):
            continue

        if FLAGS['PDF']:
            if ('.pdf' in href) or ('.PDF' in href):
                FLAG_PDF_FOUND = True
        if FLAGS['AUDIO']:
            for filt in Audio_Filter:
                if (filt in href) or (filt.upper() in href):
                    FLAG_AUDIO_FOUND = True
        if FLAGS['VIDEO']:
            for filt in Video_Filter:
                if (filt in href) or (filt.upper() in href):
                    FLAG_VIDEO_FOUND = True
        if FLAGS['IMAGE']:
            for filt in Image_Filter:
                if (filt in href) or (filt.upper() in href):
                    FLAG_IMAGE_FOUND = True
        if FLAGS['ARCHIVE']:
            for filt in Archive_Filter:
                if (filt in href) or (filt.upper() in href):
                    FLAG_ARCHIVE_FOUND = True
        if FLAG_IMAGE_FOUND or FLAG_AUDIO_FOUND or FLAG_VIDEO_FOUND or FLAG_ARCHIVE_FOUND or FLAG_PDF_FOUND:
            continue

        # Take off '/', './' , '../' of href
        while href.find('/') == 0:
            GO_BACK += 1
            href = href[1:]
        while href.find('../') == 0:
            GO_BACK += 1
            href = href[3:]
        while href.find('./') == 0:
            GO_BACK += 1
            href = href[2:]
        if len(href)-1 >= 0:
            if href[len(href)-1]=='/':
                href = href[:-1]          

        # Deal with url
        temp_url = url
        if (temp_url.rfind('.html') or temp_url.rfind('.asp') ) and temp_url.count('/')>2:
            temp_url = temp_url[:temp_url.rfind('/')]

        # Deal with GO_BACK and check whether 'http:' in href. THen combine parent address(url) and href
        while (GO_BACK>0) and temp_url.count('/')>2 and (not FLAG_HREF_HAS_HTTP):
            temp_url = temp_url[:temp_url.rfind('/')]
            GO_BACK -= 1
            if GO_BACK == 0:
                complete_url = temp_url + '/' + href

        if not FLAG_HREF_HAS_HTTP:
            complete_url = temp_url + '/'+ href

        # If complete_url is not under root domain or it's too long, drop it.
        if (root not in complete_url) or len(complete_url)>200:
            continue

        # If complete_url hasn't been traverse yet, put it into URLs and QUE.
        if complete_url not in URLs:
            URLs[complete_url] = 'Not determined'
            QUE.put(complete_url)

if __name__ == '__main__':
    main()
