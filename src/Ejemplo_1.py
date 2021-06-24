def recursion1(n):
    if n==0:
        return 4
    if n==1:
        return 3
    return 3*recursion1(n-1) + 10*recursion1(n-2) + (7.5**n)

from sympy import *
f=Function('f')
n= Symbol('n')

secuencia = (-f(n))+(3*f(n-1))+(10*f(n-2))+(7.5**n)
f0=4
f1=3

result = simplify(rsolve(secuencia,f(n), {f(0): f0, f(1): f1}))
print("La funcion que resuelve la recurrencia es: ")
print(nsimplify(result),'\n')
for i in range(10):
    print(f'Usando rsolve= {result.subs(n,i)}, {recursion1(i)=}')


