from def_dpll import dpll

our_set_of_clauses = [[1,2,3,4],[-1,-2,-3,-4],[-1,-2,-4]]
solu = {}
clauses = []
for i in range(len(our_set_of_clauses)):
	clauses.append(our_set_of_clauses[i])
	

status_dpll = dpll(clauses,solu)
if not status_dpll:
	print("unsatisfied")
else:	
	for set in solu:
		print("value of literal",set,"is",solu[set])
	


