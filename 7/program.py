from contest import *
import operator

def DamerauLevenshteinDistance(s1, s2,costs):
    _add = costs[0]
    _del = costs[1]
    _swap = costs[2]
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in xrange(-1,lenstr1+1):
        d[(i,-1)] = i+1
    for j in xrange(-1,lenstr2+1):
        d[(-1,j)] = j+1
 
    for i in xrange(0,lenstr1):
        for j in xrange(0,lenstr2):
            if s1[i] == s2[j]:
                d[(i, j)] = d[(i-1, j-1)]
            else:
                d[(i,j)] = min(
                           d[(i-1,j)] + _del, # deletion
                           d[(i,j-1)] + _add, # insertion
                           d[(i-1,j-1)] + _swap, # substitution
                          )
#            if i>1 and j>1 and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
#                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition
 
    return d[lenstr1-1,lenstr2-1]


class Test(Algorithm):

    def parse(self):
        while not(self.scanner.eos()):
            st1 = self.scanner.scan(u'[^\s]+')
            self.scanner.consume('\s+')
            st2 = self.scanner.scan(u'[^\s]+')
            self.scanner.consume('\s+')
            st1 =  repr(st1.encode('unicode_escape').decode('unicode_escape'))
            st2 =  repr(st2.encode('unicode_escape').decode('unicode_escape'))
            st1 =  repr(st1.encode('unicode_escape').decode('unicode_escape'))
            st2 =  repr(st2.encode('unicode_escape').decode('unicode_escape'))
            st1 =  repr(st1.encode('unicode_escape').decode('unicode_escape'))
            st2 =  repr(st2.encode('unicode_escape').decode('unicode_escape'))
            st1 =  repr(st1.encode('unicode_escape').decode('unicode_escape'))
            st2 =  repr(st2.encode('unicode_escape').decode('unicode_escape'))
            st1 =  repr(st1.encode('unicode_escape').decode('unicode_escape'))
            st2 =  repr(st2.encode('unicode_escape').decode('unicode_escape'))
            st1 =  repr(st1.encode('unicode_escape').decode('unicode_escape'))
            st2 =  repr(st2.encode('unicode_escape').decode('unicode_escape'))
            st1 =  repr(st1.encode('unicode_escape').decode('unicode_escape'))
            st2 =  repr(st2.encode('unicode_escape').decode('unicode_escape'))
            st1 =  repr(st1.encode('unicode_escape').decode('unicode_escape'))
            st2 =  repr(st2.encode('unicode_escape').decode('unicode_escape'))
            st1 =  repr(st1.encode('unicode_escape').decode('unicode_escape'))
            st2 =  repr(st2.encode('unicode_escape').decode('unicode_escape'))
            #st1 = st1.encode('latin1').decode('utf8')
#            #st2 = st2.encode('latin1').decode('utf8')
#            st1 =  repr(st1.encode('raw_unicode_escape').decode('raw_unicode_escape'))
#            st2 =  repr(st2.encode('raw_unicode_escape').decode('raw_unicode_escape'))
#            st1 =  repr(st1.encode('raw_unicode_escape').decode('raw_unicode_escape'))
#            st2 =  repr(st2.encode('raw_unicode_escape').decode('raw_unicode_escape'))
#            st1 =  repr(st1.encode('raw_unicode_escape').decode('raw_unicode_escape'))
#            st2 =  repr(st2.encode('raw_unicode_escape').decode('raw_unicode_escape'))
#            st1 =  repr(st1.encode('raw_unicode_escape').decode('raw_unicode_escape'))
#            st2 =  repr(st2.encode('raw_unicode_escape').decode('raw_unicode_escape'))
#            st1 =  repr(st1.encode('raw_unicode_escape').decode('raw_unicode_escape'))
#            st2 =  repr(st2.encode('raw_unicode_escape').decode('raw_unicode_escape'))
#            st1 =  repr(st1.encode('raw_unicode_escape').decode('raw_unicode_escape'))
#            st2 =  repr(st2.encode('raw_unicode_escape').decode('raw_unicode_escape'))
#            st1 =  repr(st1.encode('raw_unicode_escape').decode('raw_unicode_escape'))
#            st2 =  repr(st2.encode('raw_unicode_escape').decode('raw_unicode_escape'))
            costs = list(self.scanner.get_ints(separator=','))
            self.add(DamerauLevenshteinDistance(st1,st2,costs))
            self.scanner.next_line()
        

import sys
i = sys.stdin
o = sys.stdout
Contest(Test,input=i,output=o)