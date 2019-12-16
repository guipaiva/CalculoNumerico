import numpy as np



#define as funções de iteração
def f1(x):
    return np.cos(x)+1
def g1(x):
	return x-3*x*(np.cos(x)+1)
#def f2(x):
#    a = np.cos(2*np.pi*x)
#    b= 	x*(x-4+4/x)
#    c = 10 + b
#    xi = c - 10 * a
#    return xi
#def g2(x):

def f3(x):
	return (x**3-(3*x**2)*(2**-x)+3*x*(4**-x)-8**-x)
def g3(x):
	return x-f3(x)*x**-9
def f4(x):
    return np.sin(x)*np.sin(x**2/np.pi)
def g4(x):
	return x+((np.sin(x)*np.sin((x**2/np.pi))))/2**x
def f5(x):
    return (x-1.44)**5
def g5(x):
	return x-f5(x)*x**28

erro = 1e-6
iter_max = 10000
aprox_inicial= 3
x_aprox= aprox_inicial
raiz = np.pi

for i in range(iter_max):
	
	if abs(f1(x_aprox))<erro:
		break
	else: 
		x_aprox=g1(x_aprox)
		if abs(f1(x_aprox))<erro:
			break

print('Aprox = ',x_aprox)
print('Erro = ',abs(raiz-x_aprox)/x_aprox)
print('F(aprox) = ',f1(x_aprox))
print('Iterações = ',i+1)

