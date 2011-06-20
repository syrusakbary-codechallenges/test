from contest import *
import operator
def initialize(graph, source):
    d = {}
    p = {}
    for node in graph:
        d[node] = float('Inf')
        p[node] = None
    d[source] = 0
    return d, p

def relax(u, v, graph, d, p):
    if d[v] > d[u] + graph[u][v]:
        d[v]  = d[u] + graph[u][v]
        p[v] = u

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1):
        for u in graph:
            for v in graph[u]:
                relax(u, v, graph, d, p)
    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]
    return d, p


class Test(Algorithm):
    combos = {}

    def parse(self):
        self.scanner.consume('\s*')
        self.scanner.consume('\s*')
        while not self.scanner.eos():
            planets = int(self.scanner.scan('\d+'))
            self.scanner.consume('\s*')
            earth = int(self.scanner.scan('\d+'))
            self.scanner.consume('\s*')
            atlantis = int(self.scanner.scan('\d+'))
            self.scanner.consume('\s*')
            graph = {}
            for i in range(planets+1):
                graph[i] = {}
            while True:
                l= list(self.scanner.get_ints(separator=','))
                if len(l)==0: break
                self.scanner.consume(' *')
                i = l[0]
                j = l[1]
                d = l[2]
                #graph[i] = graph.get(i,{})
                graph[i][j] = d
                #print graph
            try:
                p,d= bellman_ford(graph,earth)
                self.add(25000+p[atlantis])
            except:
                self.add('BAZINGA')
            self.scanner.consume('\s*')

import sys
i = sys.stdin
o = sys.stdout
Contest(Test,input=i,output=o)