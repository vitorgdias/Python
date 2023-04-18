#  Formatação
#  :s - Texto (string)
#  :d - Inteiros (int)
#  :f - Números flutuantes (float)
#  :.(NÚMERO)f - Quantidade de casas decimais (float)
#  :(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

#  > - Esquerda
#  < - Direita
#  ^ - Centro

n1 = 10
n2 = 3
div = n1/n2
print('{:.2f}'.format(div))
print(f'{div:.2f}')

nome = 'Vitor'
print(f'{nome:s}')

n3 = 1
print(f'{n3:0>10}')  # 9 zeros serão adicionados à esquerda para ficar com 10 caracteres
n4 = 1150
print(f'{n4:0>10}')
print(f'{n4:0<10}')
print(f'{n4:0^10}')
print(f'{n4:0>10.2f}')

nome1 = 'Vitor'
print(f'{nome1:#^50}')

nomef = '{:@>5}'.format(nome)
print(nomef)

nomef = '{n:0<20}'.format(n=nome)
print(nomef)

sobre = 'galves'
nomef = '{0:$^50} {1:#^50}'.format(nome, sobre)
print(nomef)

nom = 'ViTu'
nom = nom.ljust(10, '#')
print(nom.lower())  #Tudo minusculo
print(nom.upper())  #Tudo maiusculo
print(nom.title())  #Primeiras letras maiusculas
