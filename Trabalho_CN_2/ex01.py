import numpy as np
from scipy.linalg import hilbert 
import time
import matplotlib.pyplot as plt 


A = hilbert(2)
b = np.zeros(2)
x = np.ones(2)
n = 300

px= []
y= []

inicio = time.time()
def gauss(A, b, x, n):
	# A = Matriz, b = solução, x = aproximação, n = número maximo de iterações 
    L = np.tril(A)
    U = A - L
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        print(x)
        """y.append(x)
        px.append(i)"""

    return x


fig=plt.figure(1)
ax = fig.add_subplot(111);
plt.plot(px,y)
t = ax.set_title("Gráfico de x"	)
ax.grid(True)

plt.show()


print('Solução matriz h2:')
print(gauss(A, b, x, n))
fim  = time.time()
print('Tempo de execução:',fim - inicio,'segundos')
