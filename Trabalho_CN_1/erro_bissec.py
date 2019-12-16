import numpy as np 
import matplotlib.pyplot as plt 

def f1(x):
	return (x-1)*(np.exp(x-2)**2)-1

a = 0
b = 3
iter_max=100
erro= 1e-6
graf_erro = np.ones((1,iter_max))
for i in range(iter_max):
	if (b - a) < erro:
		break
	aprox = (a + b)/2
	if np.sign(f1(b))*np.sign(f1(aprox))<0: 
		a = aprox       
	if np.sign(f1(a))*np.sign(f1(aprox))<0:
		b = aprox
	graf_erro[0,i] = abs((2-aprox)/aprox)

print(aprox)


fig=plt.figure(1)
ax = fig.add_subplot(111);
plt.plot(graf_erro[0,0:i])
t = ax.set_title("Gráfico do erro relativo")
t_x = ax.set_xlabel("Iteração")
t_y = ax.set_ylabel("Erro relativo")
ax.grid(True)
ax.set_xticks(np.arange(0,22,1))
ax.set_yticks(np.arange(0,0.35,0.02))

plt.show()
