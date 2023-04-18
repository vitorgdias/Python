
nome = 'Vitor'
idade = 29
altura = 1.76
peso = 83.5
ano_atual = 2022
nasc = ano_atual - idade
imc = peso/(altura**2)
print('{} tem {} anos, {}m de altura e pesa {}kg.'.format(nome, idade, altura, peso))
print('O IMC de {} é {:.2f}.'.format(nome, imc))
print('{} nasceu em {}.'.format(nome, nasc))
