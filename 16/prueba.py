#!/Users/syrus/Downloads/sage-4.7/sage -python
from sage.all import MixedIntegerLinearProgram
p = MixedIntegerLinearProgram(maximization=True)
x = p.new_variable(binary=True)
#for i in range(7):
	#p.set_binary(x[i+1])
weight = '340,355,223,243,130,240,260,155,302,130'.split(',')
production = '45,50,34,39,29,40,30,52,31'.split(',')
cows= len(production)
#objective = 0
#for l in range(len(production)):
#	objective = objective+int(production[l])*x[l+1]
import operator
objective = reduce(operator.add,[int(production[l])*x[l+1] for l in range(cows)])
p.set_objective(objective)

constraint = 0
for l in range(len(weight)):
	constraint = constraint +int(weight[l])*x[l+1]

p.add_constraint(constraint,max=2000)

#p.show()
print int(p.solve())