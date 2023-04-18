'''
Funções - def em Python (parte 1) - São criada para não repetir as coisas
'''
def funcao():
    print('Olá Mundo')

funcao()
funcao()

print('Hello World')
print('Hello World')

def funcao(msg):
    print(msg)

funcao('Posso escrever qualquer coisa')

def saudacao(msg, nome):
    print(msg, nome)

saudacao('Ola','Vitor')
saudacao('Oi','Vitor')
saudacao('Eai','João')

def saudacao1(msg='Olá', nome='Usuário'):
    print(msg, nome)

saudacao1()
saudacao1('Oi','Vitor')
saudacao1('Vitor','Ola')
saudacao1(nome='Zézinho',msg='Hi')

def saudacao2(msg1='Olá', nome1='Usuário'):
    nome1 = nome1.replace('e','3')
    msg1 = msg1.replace("e","3")
    print(msg1, nome1)

saudacao(nome='Zezinho', msg='Hello')