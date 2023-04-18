#  Listas
# nome = 'Valor'
# lista = [1, 2, 3, 4, True, 10.5, 'Vitor']
lista = ['A', 'B', 'C', 'D', 'E']

string = 'ABCDE'
print(string[1])
print(lista[1])

lista1 = ['A', 'B', 'C', 'D', 'E', 10.5]

string1 = 'ABacanaCDE'
# print(string1[1])
# print(lista1[1])
#print(lista1)
print(lista1[5])
lista1[5] = 'Qualquer coisa'
print(lista1[5])
print(lista1[0:3])  # indices mostrados 0, 1 e 2
print(lista1[:3])
print(lista1[2:])
print(lista1[-1])
print(lista1[::2])
print(lista1[::-1])