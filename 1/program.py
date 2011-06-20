from contest import *
import operator

class Test(Algorithm):
    def process (self,nums):
        return reduce(operator.add, nums)

    def parse(self):
        while not(self.scanner.eos()):
            self.add(self.process(list(self.scanner.get_ints())))
            self.scanner.next_line()
        

import sys
i = sys.stdin
o = sys.stdout
Contest(Test,input=i,output=o)