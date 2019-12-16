import numpy as np

A = np.array([[1.0, 0, -1.0], [-0.5, 1.0, -0.25], [1.0, -0.5, 1.0]])

U = np.copy(A)  
n = np.shape(U)[0]  
L = np.eye(n)  
for j in np.arange(n-1):  
    for i in np.arange(j+1,n):  
        L[i,j] = U[i,j]/U[j,j]  
        for k in np.arange(j+1,n):  
            U[i,k] = U[i,k] - L[i,j]*U[j,k]  
        U[i,j] = 0 
print('Matriz L \n',np.matrix(L))
print('Matriz U \n',np.matrix(U))