from contest import *
import operator

def min_gas (gas,M):
    G = []
    km = M
    for i in range(len(gas)-1):
        
        if (gas[i+1])>km:
            G.append(str(gas[i]))
            km = gas[i]+M
        
    return ' '.join(G) if len(G)>0 else 'No stops'
class Test(Algorithm):
    combos = {}

    def parse(self):
        self.scanner.consume('\s*')
        T = int(self.scanner.scan('\d+'))
        self.scanner.consume('\s*')
        for i in range(T):
            k = int(self.scanner.scan('\d+'))
            self.scanner.consume('\s*')
            df = int(self.scanner.scan('\d+'))
            self.scanner.consume('\s*')
            n = int(self.scanner.scan('\d+'))
            self.scanner.consume('\s*')
            gas = list(self.scanner.get_ints())
            print min_gas(gas,k)
            self.scanner.consume('\s*')

import sys
i = sys.stdin
o = sys.stdout
Contest(Test,input=i,output=o)