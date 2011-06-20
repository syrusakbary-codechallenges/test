# coding: utf-8
from contest import *
import operator
from bisect import bisect_left, bisect_right

# He creado la clase SuperRectangles que gestiona de la manera mas eficiente el problema,
# con coste (2*N+1)^2 siendo N el número de rectangulos y no H*W que correspondería
# a hacerlo de la manera mas sencilla, pero más ineficiente si H y W son ciertamente grandes.
# Lo que hace el algoritmo es partir el canvas en 'cuadraditos' para después gestionar fácilmente sus colores.
class SuperRectangles:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.x = [0,width]
        self.y = [0,height]
        self.colors = {(width,height):1}
    def color_size (self):
        colors = {}
        for i in xrange(1,len(self.x)):
            act_x = self.x[i]
            for j in xrange(1,len(self.y)):
                act_y = self.y[j]
                color = self.colors[(act_x,act_y)]
                x = self.x[i-1]
                y = self.y[j-1]
                colors[color] = colors.get(color,0)+(act_y-y)*(act_x-x)
        return colors
    def format (self,n,m):
        return max(0,min(m,n))
    def insert (self,x1,x2,y1,y2,color):
        x1,x2,y1,y2 = self.format(x1,self.width),self.format(x2,self.width),self.format(y1,self.height),self.format(y2,self.height)
        a1 = bisect_right(self.x,x1)
        a2 = bisect_right(self.x,x2)
        insert_x1 = x1!=self.x[a1-1]
        insert_x2 = x2!=self.x[a2-1]
        b1 = bisect_right(self.y,y1)
        b2 = bisect_right(self.y,y2)
        insert_y1 = y1!=self.y[b1-1]
        insert_y2 = y2!=self.y[b2-1]
        colors = self.colors.copy()
        for i in self.x[1:]:
            if insert_y1: colors[(i,y1)] = self.colors[(i,self.y[b1])]
            if insert_y2: colors[(i,y2)] = self.colors[(i,self.y[b2])]
        for j in self.y[1:]:
            if insert_x1: colors[(x1,j)] = self.colors[(self.x[a1],j)]
            if insert_x2: colors[(x2,j)] = self.colors[(self.x[a2],j)]
        if insert_x1 and insert_y1: colors[(x1,y1)] = self.colors[(self.x[a1],self.y[b1])]
        if insert_x1 and insert_y2: colors[(x1,y2)] = self.colors[(self.x[a1],self.y[b2])]
        if insert_x2 and insert_y1: colors[(x2,y1)] = self.colors[(self.x[a2],self.y[b1])]
        if insert_x2 and insert_y2: colors[(x2,y2)] = self.colors[(self.x[a2],self.y[b2])]
        if insert_x1: self.x.insert(a1,x1)
        if insert_x2: self.x.insert(a2+(1 if insert_x1 else 0),x2)
        if insert_y1: self.y.insert(b1,y1)
        if insert_y2: self.y.insert(b2+(1 if insert_y1 else 0),y2)
        for i in self.x[1:]:
            for j in self.y[1:]:
                if x1<i<=x2 and y1<j<=y2:
                    colors[(i,j)] = color
        self.colors = colors


class Rectangles(Algorithm):
    def process (self,sr):
        d = sr.color_size()
        return ' '.join(['%s %s'% (str(c),str(d[c])) for c in sorted(d.keys())])
    def parse(self):
        while not(self.scanner.eos()):
            self.scanner.consume('\s*')
            W = int(self.scanner.scan('\d+'))
            self.scanner.consume('\s*')
            H = int(self.scanner.scan('\d+'))
            self.scanner.consume('\s*')
            N = int(self.scanner.scan('\d+'))
            self.scanner.consume('\s*')
            sr = SuperRectangles(W,H)
            for i in range(N):
                x1,y1,x2,y2,color = list(self.scanner.get_ints(max=5))
                sr.insert(x1, x2, y1, y2, color)
                self.scanner.consume('\s*')
            self.add(self.process(sr))
            self.scanner.next_line()

import sys
i = sys.stdin
o = sys.stdout
Contest(Rectangles,input=i,output=o)