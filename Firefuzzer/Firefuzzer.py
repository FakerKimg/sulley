#!/usr/bin/python
import BufferOverflow
import sys
import logging

class Firefuzzer():
    def __init__(self, url, mode, detail = False):
        self.url = url
        if not self.url.startswith("http"):
            self.url = "http://" + self.url
        self.mode = mode
        self.detail = detail

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
            overflow = BufferOverflow.BufferOverflow(self.url, self.detail)
            overflow.parseInput()
            overflow.analyzeBufferOverflow()


if __name__ == "__main__":
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print "Incorrect number of parameters"
        print "Wyntax is \n\tpython Firefuzzer <url> <buffer> <detail(OPTIONAL)>"

    args = sys.argv
    detail = len(args) >= 4 and args[3] == "detail"

    fuzzer = Firefuzzer(args[1], args[2], detail)
    fuzzer.run()

