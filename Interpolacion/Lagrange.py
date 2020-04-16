def Lagrange():
  import numpy.matlib
  import numpy as np
  n=int(input('Número de datos : '))
  print('Ingrese datos separados por espacios\n  d1 d2 d3 d4 ... dn')
  d=np.matlib.zeros((3,n))
  d[0:]=list(map(float,input('Valores de x : ').strip().split()))[:n]
  d[1:]=list(map(float,input('Valores de y : ').strip().split()))[:n]
  d[2:]=np.matlib.zeros((1,n))
  for i in range(n):
    p=d[1,i]
    for j in range(n):
      if j!=i:
        p=p*(1/(d[0,i]-d[0,j]))   
    d[2,i]=p
  print('Tabla de valores de coordenadas y Lagrangianos')
  print('    x         y         L    ')
  d=np.transpose(d)
  for i in range(n):
    print('{0:^9} {1:^9} {2:^9}'.format(round(d[i,0],4),round(d[i,1],4),round(d[i,2],4)))
  #Definición de función interpolante
  def f(x,d,n):
    y=0
    for i in range(n):
      p=1
      for j in range(n):
        if j!=i:
          p=p*(x-d[j,0])
      y=y+d[i,2]*p
    return y
  #Seccion para interpolar
  xmin=d[0,0]
  xmax=d[0,0]
  for i in range(n-1):
    if xmax<d[i+1,0]:
      xmax=d[i+1,0]
    if xmin>d[i+1,0]:
      xmin=d[i+1,0]
  pre=str(input('Desea realizar alguna interpolación? (s/n): '))
  while pre=='s':
    xi=float(input('Valor de x a interpolar: '))
    while xi<xmin or xi>xmax:
      print('Error! Valor a interpolar fuera de rango de x =[',str(xmin),',',str(xmax),']')
      xi=float(input('Valor de x a interpolar: '))
    yi=f(xi,d,n)
    print('Valor interpolado: y(',str(round(xi,4)),')=',yi)
    pre=str(input('Desea realizar alguna interpolación? (s/n): '))
  #Seccion para gráficar
  import matplotlib.pyplot as plt
  xmin=d[0,0]
  xmax=d[0,0]
  for i in range(n-1):
    if xmax<d[i+1,0]:
      xmax=d[i+1,0]
    if xmin>d[i+1,0]:
      xmin=d[i+1,0]
  dis=(xmax-xmin)/999
  xg=np.matlib.zeros((1,1000))
  yg=np.matlib.zeros((1,1000))
  for i in range(1000):
    xg[0,i]=xmin+i*dis
    yg[0,i]=f(xg[0,i],d,n)
  plt.plot(d[:,0],d[:,1],'r*',xg,yg,'b-')