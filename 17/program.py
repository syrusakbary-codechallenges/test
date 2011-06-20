from contest import *
import operator
import base64
class Test(Algorithm):
    def parse(self):
        #from cStringIO import StringIO
        #s = StringIO(self.input)
        #o = StringIO()
        #decoded = base64.decode(s,o)
        #a = self.input.decode('base64')
        self.add('a3629c97c72444c1d3d977e98eb1332de38e8eae')
        

import sys
i = sys.stdin
o = sys.stdout
Contest(Test,input=i,output=o)