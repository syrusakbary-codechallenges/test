from contest import *
import operator

class Test(Algorithm):
    count = [6,2,5,5,4,5,6,3,7,6]
    def sumall (self,to,digits=2):
        if to<0: return 0
        if digits==1:
            return sum(self.count[:to+1])
        else:
            a = to//10
            b = to %10
            return self.sumall(9,1)*a + self.sumall(a-1, 1)*10+self.count[a]*(b+1)+self.sumall(b,1)
    def digival (self,digits):
        return self.count[digits//10]+self.count[digits%10]
    def partial (self,t,max,func):
        a = t // max
        b = t %  max
        return func(max-1)*a + self.sumall(a-1)*max+self.digival(a)*(b+1)+func(b)
    def minutes (self,t):
        return self.partial(t,60,self.sumall)
    def hours (self,t):
        return self.partial(t,3600,self.minutes)
    def days (self,t):
        max = 3600*24
        a = t // max
        b = t %  max
        return self.hours(max-1)*a + self.hours(b)
        
    def leds (self,time):
        return self.days(time)
    def parse(self):
        while not(self.scanner.eos()):
            self.add(self.leds(int(self.scanner.scan('\d+'))))
            self.scanner.next_line()
        

import sys
i = sys.stdin
o = sys.stdout
Contest(Test,input=i,output=o)