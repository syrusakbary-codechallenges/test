from contest import *
import operator

#Taked from http://code.activestate.com/recipes/366178-a-fast-prime-number-list-generator/ ;)
def primes(n): 
    if n==2: return [2]
    elif n<2: return []
    s=range(3,n+1,2)
    mroot = n ** 0.5
    half=(n+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]

def ispalindrome(x):
    string=str(x)
    if string==string[::-1]:
        return True
    else:
        return False

class Test(Algorithm):
    def process (self,n):
        k = []
        l = []
        for i in self.p:
            b = str(i)
            reversed = int(b[::-1])

            if ispalindrome(i): k.append(i)
            if reversed in self.p: l.append(i)

        k = filter(lambda x:x<n,k)
        l = filter(lambda x:x<n,l)
        u = sum(k)
        b = sum(l)
        return b-u
    
    def parse(self):
        n=200000
        self.p = primes(n)
        while not(self.scanner.eos()):
            number = list(self.scanner.get_ints())[0]
            self.add(self.process(number))
            self.scanner.next_line()
        

import sys
i = sys.stdin
o = sys.stdout
Contest(Test,input=i,output=o)