from contest import *
import operator

class Test(Algorithm):
    differences = {(0,1):0,
                   (1,2):4,
                   (2,3):1,
                   (3,4):1,
                   (4,5):2,
                   (5,6):1,
                   (6,7):1,
                   (7,8):4,
                   (8,9):0,
                   (9,0):1,
                   (5,0):2,
                   }
    def calcdif (self,a1,a2):
        return self.differences[(a1[0],a2[0])]+self.differences[(a1[1],a2[1])]+self.differences[(a1[2],a2[2])]+self.differences[(a1[3],a2[3])]+self.differences[(a1[4],a2[4])]+self.differences[(a1[5],a2[5])]
    def leds (self,t):
        s = 36
        ant = (0,0,0,0,0,0)
        for i in range(10):
            self.differences[(i,i)] = 0
        for i in range(1,t+1):
            hours = i//3600
            minutes = (i//60)%60
            seconds = i%60
            ant_s = (hours//10,hours%10,minutes//10,minutes%10,seconds//10,seconds%10)
            d = self.calcdif(ant,ant_s)
            s += d
            #print '%d:%d:%d - %d'%(hours,minutes,seconds,d)
            ant = ant_s
        return s
    def parse(self):
        #for i in xrange(1000):
        #    print '%d - %d#%d'%(i,self.sigdays(i),36+self.days(i))
        self.scanner.consume('\s*')
        while not(self.scanner.eos()):
            self.add(self.leds(int(self.scanner.scan('\d+'))))
            self.scanner.consume('\s*')
            self.scanner.next_line()
        

import sys
i = sys.stdin
o = sys.stdout
Contest(Test,input=i,output=o)