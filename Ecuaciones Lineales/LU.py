def LU():
  n=int(input('Número de ecuaciones del sistema: '))
  import numpy.matlib
  import numpy as np
  A=np.matlib.zeros((n,n))
  b=np.matlib.zeros((n,1))
  print('Matriz de coeficientes A: \n Escribir los coeficientes usando espacios \n ai1 ai2 ai3 ... ain')
  for i in range(n):
    A[i:]=list(map(float,input('Coeficientes ec # '+str(i+1)+' : ').strip().split()))[:n] 
  print('Vector de parámetros b:')
  for i in range(n):
    b[i:]=float(input('Resultado ec # '+str(i+1)+' : '))
  print('Matriz de coeficientes A:')
  print(A)
  print('Matriz de parámetros b:')
  print(b)
  d=np.linalg.det(A)
  if d==0:
    print('El sistema no tiene solución única!\nDeterminante de matriz de coeficientes igual a 0.')
  else:
    print('El sistema tiene solución única')
    L=np.matlib.zeros((n,n))
    U=A
    for i in range(n):
      L[i,i]=1
    for i in range(1,n):
      for j in range(i,n):
        L[j,i-1]=U[j,i-1]/U[i-1,i-1]
        U[j,:]=U[j,:]-U[j,i-1]/U[i-1,i-1]*U[i-1,:]
    print('Matriz L')
    print(L)
    print('Matriz U')
    print(U)
    z=np.matlib.zeros((n,1))
    for i in range(n):
      d=L[i,:]
      d[0,i]=0
      s=d.dot(z)
      z[i:]=b[i:]-s
    print('Vector z solución de L*z=b')
    print(z)
    x=np.matlib.zeros((n,1))
    for i in range(n):
      d=U[n-i-1,:]
      s=d.dot(x)
      x[(n-i-1),0]=(1/U[n-i-1,n-i-1])*(z[(n-i-1),0]-s[0,0])
    print('Vector x solución de Ux=z')
    print(x)