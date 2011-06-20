#!/Users/syrus/Downloads/sage-4.7/sage -python

from contest import *
import operator
#Utilizo sage para resolver el problema
from sage.all import DiGraph

class Test(Algorithm):
    def maximize (self,origin,destination,stations):
        #print origin,destination,stations
        d = DiGraph()
        d.add_edges(stations)
        return int(d.flow(origin,destination))

    def parse(self):
        while not(self.scanner.eos()):
            self.scanner.consume('\s*')
            self.scanner.consume('\d+') #El numero de estaciones
            self.scanner.consume('\s*')
            origin = self.scanner.scan('[^ ]+')
            self.scanner.consume('\s+')
            destination = self.scanner.scan('[^ ]+')
            stations = []
            while True:
                self.scanner.consume(' +')
                l = list(self.scanner.get_pattern('[^,\s]+',separator=','))
                if len(l)>0:
                    a,b,i = l
                    stations.append((a,b,int(i)))
                else:
                    break
            self.add(self.maximize(origin,destination,stations))
            self.scanner.next_line()
        

import sys
i = sys.stdin
o = sys.stdout
Contest(Test,input=i,output=o)