import math
import heapq

from os.path import basename, splitext
import re

class Scanner(object):
    def __init__(self, s):
        self.s = s
        self.offset = 0
    def eos(self):
        return self.offset == len(self.s)
    def scan(self, pattern, flags=0):
        if isinstance(pattern, basestring):
            pattern = re.compile(pattern, flags)
        match = pattern.match(self.s, self.offset)
        if match is not None:
            self.offset = match.end()
            return match.group(0)
        return None
    def next_pattern(self,pattern):
        self.scan(' +')
        return self.scan(pattern)

    def next_line(self):
        return self.scan('\n+')

    def get_pattern(self,pattern,separator=' +',operation=lambda x:x):
        while True:
            self.scan(separator)
            i = self.scan(pattern)
            if i: yield operation(i) 
            else: break
    def consume(self,*args,**kwargs):
        self.scan(*args,**kwargs)
    def get_ints(self,*args,**kwargs):
        return self.get_pattern('[+\-]?\d+',operation=int,*args,**kwargs)

    def get_str(self,*args,**kwargs):
        return self.get_pattern('\d+',operation=str,*args,**kwargs)


class Contest:
    def __init__(self,algorithm,input,output,debug=True):
        self.fi = input
        self.fo = output
        self.algorithm = algorithm(string=self.fi.read(),debug=debug)
        self.algorithm.parse()
        
        self.fo.write('\n'.join(self.algorithm.results()))
                   
class Algorithm:
    def __init__ (self,string,debug=False):
        self.debug = debug
        self.scanner = Scanner(string)
        self.out = []
    def log (self,string):
        if self.debug: print string
    def add (self,value):
        self.out.append(str(value))
    def results (self):
        return self.out
    def parse (self,string):
        pass
