import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return (x-1)*(np.exp(x-2)**2)-1

#funções de iteração
def g1(x): 
	a = np.e**((x**2)+4)
	b = np.e**(4*x)
	c = np.log(b+a)-np.log(x)-4
	return np.sqrt(c)

def g2(x):
	a = (x-2)**2
	b = np.e**a
	return (1+b)/b

def g3(x):
	a = np.log(x-1)
	b = (-1)*a+4*x-4
	return np.sqrt(b)

#Dados iniciais  
erro = 1e-6
iter_max = 50 #Limite de iteração a 50 para melhor visualização do gráfico
raiz = 2
graf_erro1 = np.zeros((1,iter_max))
graf_erro2 = np.zeros((1,iter_max))
graf_erro3 = np.zeros((1,iter_max))

x_aprox1 = 4
x_aprox2 = 4
x_aprox3 = 4

#erro relativo da função 1
for i in range(iter_max): 
	if abs(f(x_aprox1))<erro:
		break
	else: 
		x_aprox1=g1(x_aprox1)
		if abs(f(x_aprox1))<erro:
			break
	graf_erro1[0,i] = (abs((2-x_aprox1)/x_aprox1))

#erro relativo da função 2
for i in range(iter_max):
	
	if abs(f(x_aprox2))<erro:
		break
	else: 
		x_aprox2=g2(x_aprox2)
		if abs(f(x_aprox2))<erro:
			break
	graf_erro2[0,i] = (abs((2-x_aprox2)/x_aprox2))

#erro relativo da função 3
for i in range(1,iter_max):
	
	if abs(f(x_aprox3))<erro:
		break
	else: 
		x_aprox3=g3(x_aprox3)
		if abs(f(x_aprox3))<erro:
			break
	graf_erro3[0,i] = (abs((2-x_aprox3)/x_aprox3))

for i in range(50):
	print('ERRO 1=',graf_erro1[0,i])
	print('ERRO 2=',graf_erro2[0,i])
	print('ERRO 3=',graf_erro3[0,i])

#Plotagem dos gráficos 
fig = plt.figure()
ax = fig.add_subplot(111);
t_x = ax.set_xlabel("Iterações")
t_y = ax.set_ylabel("Erro Relativo")
ax.set_xticks(np.arange(0,55,5))
ax.set_yticks(np.arange(0,1.1,0.1))
l1 = plt.plot((graf_erro1[0,0:i]),label=r"$g1(x)$",color='black')
l2 = plt.plot((graf_erro2[0,0:i]),label=r"$g2(x)$",color='red')
l3 = plt.plot((graf_erro3[0,0:i]),label=r"$g3(x)$",color='blue')
l = ax.legend(loc='best')
ax.grid(True)
plt.show() 