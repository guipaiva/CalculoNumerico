import numpy as np
import matplotlib.pyplot as plt
from lagrange import *
from csv_reader import *

ano = np.arange(1980,2020)

est_anos_gas = []
est_polu_gas = []
est_anos_eta = []
est_polu_eta = []
est_anos_dis = []
est_polu_dis = []



#Gasolina
for i in range(21,38,4):
	est_anos_gas.append(ano[i])
	est_polu_gas.append(float(qtd_co_gas[i]))
print(est_anos_gas)
print("Quantidade de CO produzido através da gasolina (T/ano)")
print("Estimativa para 2018: " + str(lagrange(est_anos_gas, est_polu_gas, 2018)))
print("Estimativa oficial para 2018 MMA: 382.349")
print("Previsão para 2019: " + str(lagrange(est_anos_gas, est_polu_gas, 2019)))	
print("Estimativa oficial para 2019 MMA: 351.701\n")
qtd_co_gas.append(lagrange(est_anos_gas,est_polu_gas,2018))
qtd_co_gas.append(lagrange(est_anos_gas,est_polu_gas,2019))

#Etanol
for i in range(33,38):
	est_anos_eta.append(ano[i])
	est_polu_eta.append(float(qtd_co_eta[i]))
print(est_anos_eta) 
print("Quantidade de CO produzido através do Etanol (T/ano)")
print("Estimativa para 2018: " + str(lagrange(est_anos_eta, est_polu_eta, 2018)))
print("Estimativa oficial para 2018 MMA: 20.872")
print("Previsão para 2019: " + str(lagrange(est_anos_eta, est_polu_eta, 2019)))	
print("Estimativa oficial para 2019 MMA: 17.045\n")
qtd_co_eta.append(lagrange(est_anos_eta,est_polu_eta,2018))
qtd_co_eta.append(lagrange(est_anos_eta,est_polu_eta,2019))

#Diesel
for i in range(29,38,2):
	est_anos_dis.append(ano[i])
	est_polu_dis.append(float(qtd_co_dis[i]))
print(est_anos_dis)
print("Quantidade de CO produzido através do Diesel (T/ano)")
print("Estimativa para 2018: " + str(lagrange(est_anos_dis, est_polu_dis, 2018.0)))
print("Estimativa oficial para 2018 MMA: 173.109")
print("Previsão para 2019: " + str(lagrange(est_anos_dis, est_polu_dis, 2019.0)))	
print("Estimativa oficial para 2019 MMA: 170.027\n")
qtd_co_dis.append(lagrange(est_anos_dis,est_polu_dis,2018))
qtd_co_dis.append(lagrange(est_anos_dis,est_polu_dis,2019))

'''
est_polu_gas = []
est_polu_eta = []
est_polu_dis = []

for i in range(40):
	est_polu_gas.append(float(qtd_co_gas[i]))
	est_polu_eta.append(float(qtd_co_eta[i]))
	est_polu_dis.append(float(qtd_co_dis[i]))
div = 1000000
est_polu_gas[:]=[float(i)/ div for i in est_polu_gas]
est_polu_eta[:]=[float(i)/ div for i in est_polu_eta]
est_polu_dis[:]=[float(i)/ div for i in est_polu_dis]

fig = plt.figure(1)
ax = fig.add_subplot(111)

y1 = est_polu_gas
y2 = est_polu_eta
y3 = est_polu_dis

l1 = plt.plot(ano,y1,color='r')
l2 = plt.plot(ano,y2,color='g')
l3 = plt.plot(ano,y3,color='m')

t = ax.set_title("Gráfico da quantidade de CO emitido pela queima da Gasolina")

ax.set_yticks(np.arange(0,5,0.5))
t_x = ax.set_xlabel("Ano")
t_y = ax.set_ylabel(r"10$^6$ "+"Toneladas")
ax.grid(True)
plt.show()
'''