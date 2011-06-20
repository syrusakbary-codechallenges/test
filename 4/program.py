from contest import *
import os

class Test(Algorithm):
    def solver(self,i,cache=True):
        if cache and self.maxs.has_key(i):
            return self.maxs[i]
        s = i
        op = {}
        r = [None]
        maxs = {}        
        while True:
            op[i] = op.get(i,self.dependencies.get(i,[])[:])
            if len(op[i])>0:
                p = i
                i = op[i].pop()
                maxs[i] = max ([maxs.get(i,0), self.durations[i]])
                r.append(p)
            else:
                p = r.pop()
                if p==None:
                    break
                else:
                    #print 'Nodo: %s, duracion: %s, duracion padre: %s, maximos_padre: %s' % (i, self.durations[i], self.durations[p],maxs.get(p,[]))
                    maxs[p] = max([maxs.get(p,0),self.durations[p]+maxs[i]])
                i = p

        if not maxs.has_key(s): maxs[s] = self.durations[s]
        if cache:
            self.maxs.update(maxs)
        return maxs[s]
    
    #Manera recursiva de resolverlo
    def recursive_solver (self,i):
        deps = self.dependencies.get(i,[])
        if len(deps)>0:
            return self.durations[i]+max([self.recursive_solver(d) for d in deps])
        else:
            return self.durations[i]

    def read_db (self,name,cache=True):
        if cache:
            import marshal
            cached_db_name = name+'.marshal'
            if os.path.exists(cached_db_name):
                self.durations,self.dependencies = marshal.load(open(cached_db_name, 'rb'))
                return
        self.durations = {}
        self.dependencies = {}
        f = open(name, 'r')
        dbscanner = Scanner(f.read())
        f.close()
        dbscanner.consume('\s*#Number of tasks\s*')
        dbscanner.consume('\d+')
        dbscanner.consume('\s*#Task duration\s*')
        while True:
            l = list(dbscanner.get_ints(separator=','))
            print l
            if len(l)==0: break
            self.durations[l[0]] = l[1]
            dbscanner.next_line()
        dbscanner.scan('\s*#Task dependencies\s*')
        while True:
            l = list(dbscanner.get_ints(separator=','))
            if len(l)==0: break
            self.dependencies[l[0]] = l[1:]
            dbscanner.next_line()
        if cache:
            marshal.dump((self.durations,self.dependencies),open(cached_db_name, 'wb'))
        
    def parse(self):
        #file = os.path.join(os.path.dirname(__file__), 'in')
        file = 'in' #Para no incluirlo en el source
        self.read_db(file)
        self.maxs = {}
        while not(self.scanner.eos()):
            for i in self.scanner.get_ints(separator=','):
                self.add('%s %s'%(i,self.solver(i)))
            self.scanner.next_line()
        

import sys
i = sys.stdin
o = sys.stdout
Contest(Test,input=i,output=o)