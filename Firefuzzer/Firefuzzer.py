#!/usr/bin/python
#import BufferOverflow
import sys
import logging

class Firefuzzer():
    def __init__(self, url, mode, mode2, detail = False):
        self.url = url
        if not self.url.startswith("http"):
            self.url = "http://" + self.url
        self.mode = mode
        self.detail = detail
        self.testmode = mode2
        self.payload = []
        print detail

    def read_payload(self,filename):
        fin = open(filename,'r')
        fin.readline()
        while 1:
            tmp = fin.readline()
            if tmp == "":
                break
			self.payload.append(tmp[:-1])
            '''
            if tmp[:2] == '0x':
                self.payload.append(int(tmp[2:-1],16))
            else:
                self.payload.append(int(tmp[:-1]))
            '''
			
    def run(self):
        print ""
        print "\t8888888888 8888888 8888888b.  8888888888 8888888888 888     888 8888888888P 8888888888P 8888888888 8888888b."
        print "\t888          888   888   Y88b 888        888        888     888       d88P        d88P  888        888   Y88b "
        print "\t888          888   888    888 888        888        888     888      d88P        d88P   888        888    888 "
        print "\t8888888      888   888   d88P 8888888    8888888    888     888     d88P        d88P    8888888    888   d88P "
        print "\t888          888   8888888P\"  888        888        888     888    d88P        d88P     888        8888888P\" "
        print "\t888          888   888 T88b   888        888        888     888   d88P        d88P      888        888 T88b "
        print "\t888          888   888  T88b  888        888        Y88b. .d88P  d88P        d88P       888        888  T88b"
        print "\t888        8888888 888   T88b 8888888888 888         \"Y88888P\"  d8888888888 d8888888888 8888888888 888   T88b "
        print ""

        print "########################################################################################################################"
        print "Targeted URL : " + self.url
        print "########################################################################################################################"

        if self.mode == "buffer":
            print self.testmode
            overflow = BufferOverflow.BufferOverflow(self.url, self.detail)
            if self.testmode == '1':
                self.read_payload('integer-overflows.txt')
                print 'payload:',self.payload
                for key in self.payload:
                    overflow.parseInput(str(key))
                overflow.analyzeBufferOverflow()
        else:
            print 'else'


if __name__ == "__main__":
    print len(sys.argv)
    if len(sys.argv) != 4 and len(sys.argv) != 5:
        print "Incorrect number of parameters"
        print "Wyntax is \n\tpython Firefuzzer <url> <buffer> <detail(OPTIONAL)>"

    args = sys.argv
    detail = len(args) >= 5 and args[4] == "detail"

    fuzzer = Firefuzzer(args[1], args[2], args[3],detail)
    print args,detail
    fuzzer.run()

