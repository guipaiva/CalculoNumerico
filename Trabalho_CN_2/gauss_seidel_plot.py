import numpy as np 
from matplotlib import pyplot as plt 
from scipy.linalg import hilbert
from scipy.linalg import solve

A1 = [1, 0, -1, -0.5, 1, -0.25, 1, -0.5, 1]
b1 = [0.2, -1.425, 2]

dim = 3
N = 2000

parametro = np.linspace(-5, 5, num=50)

A = np.array(A1).reshape((dim, dim))
b = np.array(b1).reshape((1, dim))
x = np.ones(3).reshape((1, dim))
check = np.empty((dim, N))
neg = 0

y = np.empty((dim, len(parametro)))

for i in range(dim):
    y[i, :] = (b[0, i]-A[i, 0]*parametro)/A[i, 1]

check[:, 0] = x
fig = plt.figure(1)

for n in range(1, N):
    for i in range(dim):
        for j in range(dim):
            neg += -A[i, j]*x[0, j]
        neg = neg + A[i, i]*x[0, i]
        x[0, i] = (b[0, i] + neg)/A[i, i]
        neg = 0
    check[:, n] = np.copy([x])
ax = fig.add_subplot(111);
'''ax.grid(True)
ax.set_xticks(np.arange(-3,3,.25))
ax.set_yticks(np.arange(0,7,.5))'''
plt.plot(parametro, y[0, :], 'b')
plt.plot(parametro, y[1, :], 'c', label='y2')
plt.plot(parametro, y[2, :], 'b')
pontos = np.empty((dim, 3*N))

for p in range(N-1):
    pontos[:, 2*p+1] = check[0, p+1], check[1, p], check[2, p-1]
    pontos[:, 2*p] = check[:, p]

pontos[:, 2*N-1] = check[0, N-1], check[1, N-2], check [2, N-3]
pontos[:, 2*N-2] = check[:, N-1]
plt.plot(pontos[0, :], pontos[1, :], 'ko-')
plt.title('Solução: {:}'.format(check[:,-1]))

#plt.plot(check[0, :], check[1, :], 'ro-')
plt.show()
