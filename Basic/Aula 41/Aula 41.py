'''
split - Dividir uma string
join - junta uma lista
enumerate - enumera elementos da lista
'''
string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista = string.split(' ')
# print(lista)
#
lista1 = string.split(',')
# print(lista1)
palavra = ''
contagem = 0
for valor in lista:
    # print(valor)
    # print(f'A palavra {valor} apareceu {lista.count(valor)} x na frase.')
    qt = lista.count(valor)

    if qt > contagem:
        contagem = qt
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem})x')

for valor in lista1:
    print(valor.strip().capitalize())  #strip remove espaço do inicio e fim da string. Capitalize deixa a primeira letra maiuscula
