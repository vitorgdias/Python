# Desempacotamento

lista = ['Luiz', 'João', 'Maria']
n1, n2, n3 = lista

print(n2)

n1, n2, *outra_lista = lista
print(n1, n2)

lista1 = ['Luiz', 'João', 'Maria',1,2,4,6,5]
n1, n2, *outra_lista1 = lista1
print(n1, n2)

lista2 = ['Luiz', 'João', 'Maria',1,2,4,6,5]
n1, n2, *outra_lista2, ultimo = lista2
print(ultimo)
print(outra_lista2)

lista3 = ['Luiz', 'João', 'Maria',1,2,4,6,5]
*outra_lista3, n1, n2 = lista3
print(outra_lista3)