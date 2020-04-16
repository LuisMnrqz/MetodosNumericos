def biseccion():
  def f(x):
    return x**3-1
  print('Solución de: x^3-1=0')
  a=float(input('a='))
  b=float(input('b='))
  t=float(input('Tol(%)='))
  e=t+1
  i=0
  print(' i      a         b         c       f(a)      f(b)      f(c)      e(%)   ')
  while e>=t:
    i=i+1
    c=(a+b)/2
    if i>1:
      e=abs((x-c)/c)*100
      print('{0:^3} {1:^9} {2:^9} {3:^9} {4:^9} {5:^9} {6:^9} {7:>9}'.format(int(i),round(a,4),round(b,4),round(c,4),round(f(a),4),round(f(b),4),round(f(c),4),round(e,4)))
    else:
      er='-'
      print('{0:^3} {1:^9} {2:^9} {3:^9} {4:^9} {5:^9} {6:^9} {7:>9}'.format(int(i),round(a,4),round(b,4),round(c,4),round(f(a),4),round(f(b),4),round(f(c),4),er))
    if f(a)*f(c)<0:
      b=c
    else:
      a=c
    x=c
  if e>0:
    print('Solución aproximada encontrada en x = ',c)
  else:
    print('Solución exacta encontrada en x = ',c)