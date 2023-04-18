
nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))
menor = 20
maior = 30

if idade >= menor and idade <= maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')