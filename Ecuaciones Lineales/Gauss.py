def Gauss():
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
    Au=np.concatenate((A,b),axis=1)
    print('Matriz aumentada de sistema de ecuaciones A|b')
    print(Au)
    print('Eliminación Gaussiana a triangular superior')
    for j in range(n):
      Au[j,:]=Au[j,:]/Au[j,j]
      A[j,:]=A[j,:]/A[j,j]
      print(Au)
      for i in range(j+1,n):
        Au[i,:]=Au[i,:]-Au[i,j]*Au[j,:]
        A[i,:]=A[i,:]-A[i,j]*A[j,:]
        print(Au)
    b=Au[:,n]
    x=np.matlib.zeros((n,1))
    for i in range(n):
      d=A[n-i-1,:]
      d[0,n-i-1]=0
      s=d.dot(x)
      x[(n-i-1),0]=b[(n-i-1),0]-s[0,0]
    print('Vector solución x')
    print(x)