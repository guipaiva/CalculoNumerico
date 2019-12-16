def lagrange(ano, poluicao, valor):
	L = []
	for i in range(len(ano)):
		numerador_prod = 1
		denominador_prod = 1
		for j in range(len(ano)):
			if(j!=i):
				numerador_prod*=(valor - ano[j])
				denominador_prod*=(ano[i] - ano[j])

		L.append(numerador_prod/denominador_prod)

	for i in range(len(L)):
		L[i]*=poluicao[i]
	return sum(L)
