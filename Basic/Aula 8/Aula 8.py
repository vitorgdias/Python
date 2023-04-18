#  Entrada de dado
'''
nome = input("Qual o seu nome? ")  #retorna um resultado em string
print(f'O usuário digitou {nome} e o tipo da variável é '
      f'{type(nome)}')
'''

nome = input("Qual o seu nome? ")
idade = input('Qual a sua idade? ')
'''
nasc = 2022-idade  #Irá ficar errado, pois idade é retornada em string
print()
print(f'{nome} tem {idade} anos.')
'''

nasc = 2022 - int(idade)  #Tem que transformar em inteiro (int)
print(f'{nome} tem {idade} anos. '
      f'{nome} nasceu em {nasc}')
