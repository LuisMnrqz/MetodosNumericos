def NewtonRaphson():
    def f(x):
      return x**3 - 1
    def fp(x):
      return 3*x**2
    print('Solución de: x^3-1=0')
    xi = float(input('x0 ='))
    t = float(input('Tol(%) ='))
    imax=float(input('Iteraciones máximas : '))
    e = t + 1
    i = 0
    print(' i    x(i)     f(x(i))  fp(x(i))   x(i+1)      e(%)  ')
    while e >= t and i<=imax:
        i = i + 1
        if fp(xi)==0:
          break
        x1=xi-f(xi)/fp(xi)
        e = abs((x1 - xi) / x1)*100
        print('{0:^3} {1:^9} {2:^9} {3:^9} {4:^9} {5:>9}'.format(int(i), round(xi, 4), round(f(xi), 4), round(fp(xi), 4),round(x1,4),round(e, 4)))
        xi = x1
    if fp(xi)==0:
      print('Solución divergente! Derivada = 0.')
    if e>100*t:
      print('Solución probablemente divergente!')
    if e > 0:
      print('Solución aproximada encontrada en x = ', x1)
    else:
      print('Solución exacta encontrada en x = ', x1)