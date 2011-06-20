#!/Users/syrus/Downloads/sage-4.7/sage -python

from contest import *
import operator
#Utilizo sage para resolver el problema
from sage.all import MixedIntegerLinearProgram

class Test(Algorithm):
    def minimize (self,cows,max_weight,cow_weight,cow_production):
        p = MixedIntegerLinearProgram(maximization=True)
        cow = p.new_variable(binary=True)
        objective_production = [cow_production[l]*cow[l] for l in range(len(cow_production))]
        objective = reduce(operator.add,objective_production)
        p.set_objective(objective)
        constraint_weight = [cow_weight[l]*cow[l] for l in range(len(cow_weight))]
        constraint = reduce(operator.add,constraint_weight)
        p.add_constraint(constraint,max=max_weight)
        return int(p.solve())

    def parse(self):
        while not(self.scanner.eos()):
            cows = int(self.scanner.scan('\d+'))
            self.scanner.consume('\s+')
            max_weight = int(self.scanner.scan('\d+'))
            self.scanner.consume('\s+')
            cow_weight = list(self.scanner.get_ints(separator=','))
            self.scanner.consume('\s+')
            cow_production = list(self.scanner.get_ints(separator=','))
            self.add(self.minimize(cows,max_weight,cow_weight,cow_production))
            self.scanner.next_line()
        

import sys
i = sys.stdin
o = sys.stdout
Contest(Test,input=i,output=o)