from contest import *
import operator

def lights(l,i):
    i_mod = i%2
    on =[]
    for n in range(l):
        if n<i and n%2!=i_mod: on.append(str(n))
    return ' '.join(on) if len(on)>0 else 'All lights are off :('

class Test(Algorithm):
    def parse(self):
        self.scanner.consume('\s*')
        self.scanner.consume('\d+')
        self.scanner.consume('\s*')
        while not(self.scanner.eos()):
            l = int(self.scanner.scan('\d+'))
            self.scanner.consume('\s*')
            i = int(self.scanner.scan('\d+'))
            self.add(lights(l,i))
            self.scanner.next_line()
        

import sys
i = sys.stdin
o = sys.stdout
Contest(Test,input=i,output=o)