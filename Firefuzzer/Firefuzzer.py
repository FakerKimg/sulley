#!/usr/bin/python
import BufferOverflow
import sys
import logging
import re

class Firefuzzer():
    def __init__(self, source, stype, sleep_time = 0.1, mode = ''):
        self.source = source
        if stype == 'url' and not self.source.startswith("http"):
            self.source = "http://" + self.source
        self.testmode = mode
        self.stype = stype
        self.sleep = sleep_time
        print sleep_time,mode
	
    def readlink(self):
        f = open(self.source,'r')
        self.link = []
        while True:
            tmp = f.readline()
            if tmp == '':
                break
            if not tmp.startswith("http"):
                tmp = "http://" + tmp
            self.link.append(tmp[:-1])
        
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
        print "Targeted source : ",
        if self.stype == 'file':
            print 'File:',self.source
        else:
            print self.source
        print "########################################################################################################################"

        if self.stype == "url":
            overflow = BufferOverflow.BufferOverflow(self.source)
            overflow.parse_html()
	    if self.testmode == 'auto':
                overflow.autotest(self.sleep)
            elif self.testmode == 'html':
                overflow.test_input(self.sleep)
            else:
                overflow.parseInput()
            overflow.analyzeBufferOverflow()   
        elif self.stype == 'file':
            self.readlink()
            for u in self.link:
                print 'Target url:',u
                overflow = BufferOverflow.BufferOverflow(u)
                overflow.parse_html()
                if self.testmode == 'auto':
                    overflow.autotest(self.sleep)
                elif self.testmode == 'html':
                    overflow.test_input(self.sleep)
                else:
                    overflow.parseInput()
                overflow.analyzeBufferOverflow()

               


if __name__ == "__main__":
    if len(sys.argv) <3 or len(sys.argv)>5:
        print "Incorrect number of parameters"
        print "Wyntax is \n\tpython Firefuzzer <source> <source_type> (<sleep_time>) (<test_mode>)"

    args = sys.argv
    if len(args)==3:
        fuzzer = Firefuzzer(args[1], args[2])
    elif len(args)==4:
        if re.match('([0-9]+\.[0-9]+)|(\d)',args[3]):
            fuzzer = Firefuzzer(args[1], args[2], sleep_time = args[3])
        else:
            fuzzer = Firefuzzer(args[1], args[2], mode = args[3])
    else:
        fuzzer = Firefuzzer(args[1], args[2], args[3], args[4])
    #print args,detail
    fuzzer.run()

