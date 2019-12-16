import csv


qtd_co_gas = []
qtd_co_dis = []
qtd_co_eta = []
#lendo arquivos csv
with open('poluicao_gasolina.csv') as csvfile: 	
	leitor_csv = csv.reader(csvfile, delimiter=',')
	next(leitor_csv,None)
	for linha in leitor_csv:
		qtd_co_gas.append(linha[4])

with open('poluicao_etanol.csv') as csvfile: 	
	leitor_csv = csv.reader(csvfile, delimiter=',')
	next(leitor_csv,None)
	for linha in leitor_csv:
		qtd_co_eta.append(linha[3])

with open('poluicao_diesel.csv') as csvfile: 	
	leitor_csv = csv.reader(csvfile, delimiter=',')
	next(leitor_csv,None)
	for linha in leitor_csv:
		qtd_co_dis.append(linha[7])
