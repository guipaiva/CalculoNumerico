import numpy as np

#define as funções de iteração e suas derivadas 
def f1(x):
    return np.cos(x)+1
def df1(x):
	return -np.sin(x)
def f2(x):
    return 10+(x-2)**2-10*np.cos(2*np.pi*x)
def df2(x):
	return 2*x+20*np.pi*np.sin(2*np.pi*x)-4
def f3(x):
    return (x**3-(3*x**2)*(2**-x)+3*x*(4**-x)-8**-x)
def df3(x):
	return (3*x**2-3*(2**(1-x)*x-np.log(2)*2**-x*x**2)+3*(4**-x-np.log(2)*2**(-2*x+1)*x)+3*np.log(2)*8**-x)
def f4(x):
    return np.sin(x)*np.sin(x**2/np.pi)
def df4(x):
	return np.cos(x)*np.sin(x**2/np.pi+(2*x*np.cos(x**2/np.pi)*np.sin(x))/np.pi)
def f5(x):
    return (x-1.44)**5
def df5(x):
	return (5*(x-1.44)**4)

#Define os valores para iteração
iter_max = 10000
x_inicial = 2 
x=[]
x.append(x_inicial) 
erro=1e-6 
raiz=np.pi

#iterações para calculo da raiz
for i in range(1,iter_max):
	x.append((x[i-1]-(f1(x[i-1]))/df1(x[i-1])))
	if abs(x[i]-x[i-1])<erro: 
		break

print('Aprox = ',x[i])
print('Erro = ',abs((raiz-x[i])/x[i]))
print('F(aprox) = ',f1(x[i]))
print('Iterações = ',i+1)