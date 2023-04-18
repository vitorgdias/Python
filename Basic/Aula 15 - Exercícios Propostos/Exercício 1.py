n = input('Digite um número inteiro: ')
if n.isdigit():
    n = int(n)
    if n % 2 == 0:
        print(f'{n} é um número par')
    else:
        print(f'{n} é um número impar')
else:
    print('Erro, você não digitou um número inteiro')

# Invertido:
'''
if not n.isdigit():
    print('Erro, você não digitou um número inteiro')
else:
    n = int(n)
    if n % 2 == 0:
        print(f'{n} é um número par')
    else:
        print(f'{n} é um número impar')
'''