#Laços While

'''
while True:
    nome = input('Qual o seu nome? ')
    print(f'Olá{nome}!')

print('Não é executado.')
'''

'''
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue  #Como x = 3, ele cai na condição, soma +1 e continua o laço, sem imprimir o nº3.

    print(x)
    x = x+1

print('Acabou')
'''
'''
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break  #Finaliza o looping (laço) tanto para while quanto para for

    print(x)
    x = x+1

print('Acabou')
'''
'''
Coordenadas
x = 0  #linha

while x < 10:
    y = 0  # coluna
    while y < 5:
        print(f'{x},{y}')
        y += 1

    x += 1  #É o mesmo que escrever x = x + 1

print('Acabou!')
'''

while True:
    print()
    sair = input('Deseja sair? [s] ou [n]: ')
    if sair == 's':
        break
    n1 = input('Digite um número: ')
    n2 = input('Digite um outro número: ')

    if not n1.isnumeric() or not n2.isnumeric():
        print('Você não digitou um número.')
        continue
    n1 = int(n1)
    n2 = int(n2)
    operador = input('Digite um operador: ')
    if operador == '+':
        print(n1 + n2)
    elif operador == '-':
        print(n1 - n2)
    elif operador == '*':
        print(n1 * n2)
    elif operador == '/':
        print(n1 / n2)
    else:
        print('Operador inválido')