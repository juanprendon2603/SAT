

def imprimir(xsat, clausulas, variables):
	print("p cnf "+str(variables)+" "+str(clausulas))
	out = ""
	for i in range(clausulas):
		for j in range(len(xsat[i])):
			out += str(xsat[i][j]) + " "
		out += str(0)
		out += "\n"
	print(out)

