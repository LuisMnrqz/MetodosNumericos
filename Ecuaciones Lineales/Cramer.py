def Cramer():
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
    x=np.matlib.zeros((n,1))
    C=np.matlib.zeros((n,n))
    for i in range(n):
      for j in range(n):
        if i==j:
          C[:,j]=b
        else:
          C[:,j]=A[:,j]
      print('Matriz modificada para la incógnita x'+str(i+1))
      print(C)
      d1=np.linalg.det(C)
      x[i:]=d1/d
    print('Vector solución')
    print(x)