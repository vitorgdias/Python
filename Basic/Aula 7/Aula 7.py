
nome = 'Vitor Galves'  #string
idade = 28  #int
altura = 1.76  #float
e_maior = idade > 18  #bool
peso = 82
imc = peso/(altura**2)

print(nome, 'tem', idade, 'de idade e seu IMC é', imc)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')  #.2f significa 2 casas flutuantes

print('{} tem {} anos e seu imc é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos e seu imc é {2}'.format(nome, idade, imc))
print('{n} tem {i} anos e seu imc é {im}'.format(n=nome, i=idade, im=imc))