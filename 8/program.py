from contest import *
import operator

import functools

def cached(func):
  cache = {}
  def template(*args): #: template is wrapper; func is wrapped
    key = (func, )+args
    try:
      ret = cache[key]
    except KeyError:
      ret = func(*args)
      cache[key] = ret
    else:
      pass
    return ret

  functools.update_wrapper(template, func)
  return template


def LongestCommonSubstring(S1, S2):
    M = [[0]*(1+len(S2)) for i in xrange(1+len(S1))]
    longest, x_longest = 0, 0
    for x in xrange(1,1+len(S1)):
        for y in xrange(1,1+len(S2)):
            if S1[x-1] == S2[y-1]:
                M[x][y] = M[x-1][y-1] + 1
                if M[x][y]>longest:
                    longest = M[x][y]
                    x_longest  = x
            else:
                M[x][y] = 0
    return S1[x_longest-longest: x_longest]

  
class Test(Algorithm):
    def parse(self):
        while not(self.scanner.eos()):
            st1 = self.scanner.scan(u'[^\s]+')
            self.scanner.consume('\s+')
            st2 = self.scanner.scan(u'[^\s]+')
            self.scanner.consume('\s+')
            self.add(LongestCommonSubstring(st1,st2))
            self.scanner.next_line()
        

import sys
i = sys.stdin
o = sys.stdout
Contest(Test,input=i,output=o)