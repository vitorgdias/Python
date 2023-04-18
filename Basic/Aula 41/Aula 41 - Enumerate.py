
string = 'O Brasil é penta;'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])

lista1 = [
    [1,2],
    [3,4],
    [5,6],
]
for v in lista1:
    print(v)
for v in lista1:
    print(v[0])
for v in lista1:
    print(v[0], v[1])

lista2 = [
    [0,'vitor'],
    [1,'joão'],
    [2,'maria'],
]

for ind, nome in lista2:
    print(ind, nome)

lista3 = ['vitor','joão','maria']

for ind, nome in enumerate(lista3):
    print(ind, nome)

n1, n2, n3 = lista3

print(n2)
