# Enumerate

lista = [
#      0       1        2         Indice da lista filha (lista dentro da lista
    ['Edu', 'João', 'Luiz'],  # 0
    ['Maria', 'Aline', 'Joana'],  # 1
    ['Helena', 'Ed', 'Lu'],  # 2
]
print(lista[2])
print(lista[1][2])
enumerada = enumerate(lista)
print(enumerada)
print(list(enumerada))

enumerada = list(enumerate(lista))
print(enumerada[1][1])
print(enumerada[1][1][2])

for v1, v2 in enumerate(lista):
    print(v1, v2)

for v1, v2 in enumerate(lista, 53):
    print(v1, v2)