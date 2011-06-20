from contest import *
import operator

class TLang(Algorithm):
    def process (self,op,nums):
        operations = {
                      '=':operator.add,
                      '#':operator.mul,
                      '@':operator.sub
                      }
        if len(nums)==1 and op=='@': return -nums[0]
        return reduce(operations.get(op,lambda x,y: 0), nums)

    def operate (self):
        start = self.scanner.scan('\^')
        
        if not(start):
            l = self.scanner.get_ints(separator=' +')
            return (list(l) if l else [])
        else:
            op = self.scanner.scan('=|#|@')
            reduced = []
            while not(self.scanner.scan('\$')):
                reduced += self.operate()
            return [self.process(op,reduced)]
            
    def parse(self):
        while not(self.scanner.eos()):
            r = self.operate()
            self.add(r[0])
            self.scanner.next_line()
        

import sys
i = sys.stdin
o = sys.stdout
Contest(TLang,input=i,output=o)