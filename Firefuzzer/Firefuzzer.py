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
        if self.mode == "buffer":
            overflow = BufferOverflow.BufferOverflow(self.url, self.detail)
            overflow.parseInput()
            overflow.analyzeBufferOverflow()


if __name__ == "__main__":
    args = sys.argv
    detail = len(args) >= 4 and args[3] == "detail"

    fuzzer = Firefuzzer(args[1], args[2], detail)
    fuzzer.run()

