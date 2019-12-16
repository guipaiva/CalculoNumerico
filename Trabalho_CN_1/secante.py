import numpy as np 

#define as funções de iteração
def f1(x):
    return np.cos(x)+1
def f2(x):
    return 10+(x-2)**2-10*np.cos(2*np.pi*x)
def f3(x):
    return (x**3-(3*x**2)*(2**-x)+3*x*(4**-x)-8**-x)
def f4(x):
    return np.sin(x)*np.sin(x**2/np.pi)
def f5(x):
    return (x-1.44)**5

#define os valores para iteração
erro = 1e-6
x = []
iter_max=10000
A=2
B=3
raiz = np.pi
x.append(A)
x.append(B)

#iterações para o cálculo da raiz
for i in range(2,iter_max):
    fa=f1(x[i-2])
    fb=f1(x[i-1])
    x.append(x[i-1]-(fb*(x[i-1]-x[i-2]))/(fb-fa))
    if abs(x[i]-x[i-1]) <erro:
        break
print('Aprox = ',x[i])
print('Erro = ',abs((raiz-x[i])/x[i]))
print('F(aprox) = ',f1(x[i]))
print('Iterações = ',i+1)

