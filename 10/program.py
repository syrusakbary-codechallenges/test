from contest import *
import operator

class Test(Algorithm):
    combos = {}
    def hash (self,keys):
        return str(sorted(keys))
    def add_combo (self,keys,name):
        key = self.hash(keys)
        if self.combos.has_key(key): return
        self.combos[key] = name
    def get_combo (self,keys):
        return self.combos.get(self.hash(keys),'')

    def parse(self):
        self.scanner.consume('\s*')
        n = int(self.scanner.scan('\d+'))
        self.scanner.next_line()
        for i in range(n):
            keys = list(self.scanner.get_pattern('\w{0,6}'))
            self.scanner.next_line()
            name = self.scanner.scan('\w+')
            self.add_combo(keys,name)
            self.scanner.consume('\s*')
        t = int(self.scanner.scan('\d+'))
        for i in range(t):
            self.scanner.consume('\s*')
            self.add(self.get_combo(list(self.scanner.get_pattern('\w{0,6}'))))
            self.scanner.next_line()

import sys
i = sys.stdin
o = sys.stdout
Contest(Test,input=i,output=o)