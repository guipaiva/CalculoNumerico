import numpy as np

#define as funções de iteração
def f1(x):
    return np.cos(x)+1
def f2(x):
    return 10+(x-2)**2-10*np.cos(2*np.pi*x)
def f3(x):
    return (x**3-(3*x**2)*(2**-x)+3*x*(4**-x)-8**-x)
def f4(x):
    return np.sin(x)*np.sin((x**2)/np.pi)
def f5(x):
    return (x-1.44)**5

#define os valores para iteração
a =  0 #valor inicial do intervalo
b =  3.8  #valor final do intervalo
iter_max = 10000
erro = 1e-6
raiz = np.pi

#iterações para calculo da raiz
for i in range(iter_max):
    if(b-a) < erro:
        break
    aprox = (a + b)/2
    #atualizar o f para a função escolhida
    if np.sign(f1(b))*np.sign(f1(aprox))<0: 
        a = aprox       
    if np.sign(f1(a))*np.sign(f1(aprox))<0:
        b = aprox

print('Aprox = ',aprox)
print('Erro = ',abs((raiz-aprox)/aprox))
print('F(aprox) = ',f1(aprox))
print('Iterações = ',i+1)