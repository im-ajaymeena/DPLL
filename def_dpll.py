import timeit

def dpll(our_clauses, solu):
	if(len(our_clauses) == 0):	
		return True	
	for clause in our_clauses:	
		if(len(clause) == 1):	
			return False	
	####This checks presence of unit clause
	for clause in our_clauses:	
		index = 0
		if(len(clause) == 2):
			check_literal = clause[0]
			if check_literal < 0:	
				solu[-1*check_literal] = 0	
			else:	
				solu[check_literal] = 1	
			our_clauses.remove(clause)
			index = 0
			####This performs pure literal elimination
			while (index != len(our_clauses)):	
				temp_bool = False	
				for lit in our_clauses[index]:	
					if lit == check_literal:	
						temp_bool = True	
						break	
					elif (lit == (-1*check_literal)):	
						our_clauses[index].remove(lit)	
				if temp_bool:	
					our_clauses.pop(index)
					index = index - 1
				index = index + 1
			return dpll(our_clauses[:],solu)
	
	
	smallest_one = our_clauses[0]
	for clause in our_clauses: 
		if len(smallest_one) > len(clause):
			smallest_one = clause
	check_literal = smallest_one[0]
	tempour_clauses = our_clauses[:]
	tempour_clauses.remove(smallest_one)

	#####This performs splitting
	index = 0
	while (index != len(tempour_clauses)):
		temp_bool = False
		for lit in tempour_clauses[index]:
			if lit == check_literal:
				temp_bool = True
				break
			elif (lit == (-1*check_literal)):
				tempour_clauses[index].remove(lit)
		if temp_bool:
			tempour_clauses.pop(index)
			index = index - 1
		index = index + 1
	tempSolve = solu
	status_dpll = dpll(tempour_clauses,solu)
	if status_dpll:
		if check_literal < 0:
			solu[-1*check_literal] = 0
		else:
			solu[check_literal] = 1
		return status_dpll
	else:
		solu = tempSolve[:]
		check_literal = (-1*check_literal)
		tempour_clauses = our_clauses[:]
		index = 0
		while (index != len(tempour_clauses)):
			temp_bool = False
			for lit in tempour_clauses[index]:
				if lit == check_literal:
					temp_bool = True
					break
				elif (lit == (-1*check_literal)):
					tempour_clauses[index].remove(lit)
			if temp_bool:
				tempour_clauses.pop(index)
				index = index -1
			index = index + 1
		if check_literal < 0:
			solu[-1*check_literal] = 0
		else:
			solu[check_literal] = 1
	return dpll(tempour_clauses,solu)
