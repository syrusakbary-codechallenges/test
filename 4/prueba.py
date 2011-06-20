task_dur = {
	0:2,
	1:3,
	2:4,
	3:9,
	4:7,
	5:9,
	6:1
}
task_dep = {
	0:[4],
	6:[4],
	3:[0,1,2,6],
	4:[5]
}

solve =[ 3,1,4]

def solver(i):
	deps = task_dep.get(i,[])
	if len(deps)>0:
		return task_dur[i]+max([solver(d) for d in deps])
	else:
		return task_dur[i]

print solver(6)