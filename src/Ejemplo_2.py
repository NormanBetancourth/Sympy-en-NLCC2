def recursion2(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return  recursion2(n-1) + (6*recursion2(n-2)) + 2**n

P = Function('P')
x = Symbol('x', integer=true)

secuencia2 =(-P(x)) + P(x-1) + (6*P(x-2)) + 2**x
P0=0
P1=1

result2 = simplify(rsolve(secuencia2,P(x), {P(0): P0, P(1): P1}))
print("La funcion que resuelve la recurrencia es: ")
print(result2,'\n')
for i in range(10):
    print(f'Usando rsolve= {simplify(result2.subs(x,i))}, {recursion2(i)=}')
