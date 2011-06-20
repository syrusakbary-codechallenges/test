from contest import *
import operator

from PIL import Image
import os

class Test(Algorithm):
    indexes = {'R':0,
               'G':1,
               'B':2}
    def pixels (self,color,line):
        if not self.indexes.has_key(color): return 1
        i = self.indexes[color]
        r = range(self.rgb.size[0]) if 0<=line<=self.rgb.size[1] else []
        return sum([self.rgb.getpixel((j, line))[i] for j in r])+1
    def parse(self):
        imagename = 'trabaja.bmp'
        self.rgb = Image.open(os.path.join(os.path.dirname(__file__),imagename)).convert('RGB')
        self.scanner.consume('\s*')

        while not(self.scanner.eos()):
            color = self.scanner.scan('R|G|B')
            line = int(self.scanner.scan('\d+'))
            self.add(self.pixels(color,line))
            self.scanner.consume('\s*')
            self.scanner.next_line()
        

import sys
i = sys.stdin
o = sys.stdout
Contest(Test,input=i,output=o)