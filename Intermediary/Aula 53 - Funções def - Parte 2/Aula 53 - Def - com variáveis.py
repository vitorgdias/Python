def divisao(n1,n2):
    return n1/n2

divide = divisao(8,2)
print(divide)

def divisao1(n1,n2):
    if n2 > 0:
        return n1/n2

divide1 = divisao1(8,0)

if divide1:
    print(divide1)
else:
    print('Conta inválida')

def divisao2(n1,n2):
    if n2 == 0:
        return
    return n1 / n2

divide2 = divisao2(8,-1)

if divide2:
    print(divide2)
else:
    print('Conta inválida')

def f(var):
    print(var)

def dumb():
    return f

var = dumb()('Meu valorzin')

def f1(var):
    print(var)

def dumb1():
    return f1

var1 = dumb1()
print(id(var1),id(f1))

if var1==f1:
    print('Var é igual a f')
else:
    print('Não é igual')

def dumb2():
    return ('Vitor','Galves')

print(dumb2())
var3 = dumb2()
print(var3, type(var3))