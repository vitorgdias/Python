
nome = input('Digite o seu nome: ')

if nome:
    print(nome)
else:
    print('Você não digitou nada.')

n = input('Digite o seu nome: ')

print(n or 'Você não digitou nada')

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Luiz'
variavel = a or b or c or d or e or f or g
print(variavel)
