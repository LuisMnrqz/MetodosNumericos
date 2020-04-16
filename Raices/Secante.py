def Secante():
    def f(x):
      return x**3 - 1
    print('Solución de: x^3-1=0')
    xa = float(input('x(-1) ='))
    xb = float(input('x(0) = '))
    t = float(input('Tol(%) ='))
    imax=float(input('Iteraciones máximas : '))
    e = t + 1
    i = 0
    print(' i   x(i-1)     x(i)     f(x(i))  fp(x(i))   x(i+1)      e(%)  ')
    while e >= t and i<=imax:
        i = i + 1
        fp=(f(xa)-f(xb))/(xa-xb)
        if fp==0:
          break
        x1=xb-f(xb)/fp
        e = abs((x1 - xb) / x1)*100
        print('{0:^3} {1:^9} {2:^9} {3:^9} {4:^9} {5:^9} {6:>9}'.format(int(i), round(xa, 4), round(xb,4),round(f(xa), 4), round(fp, 4),round(x1,4),round(e, 4)))
        xa = xb
        xb = x1
    if fp==0:
      print('Solución divergente! Derivada = 0.')
    if e>10*t:
      print('Solución probablemente divergente!')
    if e > 0:
      print('Solución aproximada encontrada en x = ', x1)
    else:
      print('Solución exacta encontrada en x = ', x1)