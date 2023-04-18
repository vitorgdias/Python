
nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))
limite = 18
if idade >= limite:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')
