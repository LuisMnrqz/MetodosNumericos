Bairstowdef Bairstow():
  import math
  n=int(input('Grado de polinomio (n) : '))
  n=n+1
  p=[0]*n
  print('Coeficientes del polinomio')
  print('a_n*x^n+a_(n-1)*x^(n-1)+...+a_2x^2+a_1*x+a_0')
  for i in range(n):
    p[i]=float(input('a_'+str(n-i-1)+' = '))
  r=float(input('r inicial : '))
  s=float(input('s inicial : '))
  t=float(input('Tolerancia (%) : '))
  root=[0]*(n-1)
  while n>3:
    print('Coeficientes de polinomio')
    print(p)
    e=t+1
    j=0
    while e>=t:
      j=j+1
      b=[0]*(n)
      c=[0]*(n)
      print('Iteración # ',int(j),' [r,s] = [',round(r,4),',',round(s,4),']')
      b[0]=p[0]
      b[1]=p[1]+r*b[0]
      c[0]=b[0]
      c[1]=b[1]+r*c[0]
      for j in range(2,n):
        b[j]=p[j]+r*b[j-1]+s*b[j-2]
        c[j]=b[j]+r*c[j-1]+s*c[j-2]
      print('Vector de coeficientes b : ',b)
      print('Vector de coeficientes c : ',c)
      A=[[c[n-3],c[n-4],-b[n-2]],[c[n-2],c[n-3],-b[n-1]]]
      print('Matriz aumentada de sistema de ecuaciones A*D=b => A|b =')
      print(A)
      ds=(-b[n-1]/c[n-2]+b[n-2]/c[n-3])/(c[n-3]/c[n-2]-c[n-4]/c[n-3])
      dr=-b[n-2]/c[n-3]-ds*c[n-4]/c[n-3]
      r=r+dr
      s=s+ds
      err=abs(dr/r)*100
      ers=abs(ds/s)*100
      if err>ers:
        e=err
      else:
        e=ers
      print('   dr        ds        err       ers   ')
      print('{0:^9} {1:^9} {2:^9} {3:^9}'.format(round(dr,4),round(ds,4),round(err,4),round(ers,4)))
    r1=(r+(r**2+4*s)**0.5)/2
    r2=(r-(r**2+4*s)**0.5)/2
    print('Raíces encontradas:[',r1,',',r2,4,']')
    root[n-2]=r1
    root[n-3]=r2
    n=n-2
    p=[0]*(n)
    for k in range(n):
      p[k]=b[k]
  if n==3:
    print('Coeficientes del polinomio')
    print(p)
    r1=(-p[1]+((p[1])**2-4*p[0]*p[2])**0.5)/(2*p[0])
    r2=(-p[1]-((p[1])**2-4*p[0]*p[2])**0.5)/(2*p[0])
    root[0]=r1
    root[1]=r2
    print('Raíces encontradas:[',r1,4,',',r2,4,']')
  elif n==2:
    print('Coeficientes del polinomio')
    print(p)
    x=-p[1]/p[0]
    root[0]=x
    print('Raíz : ',x)
  print('Vector de raíces del polinomio')
  print(root)