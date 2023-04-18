'''
Funções def - Return  -Parte 2
'''
def funcao(var):
    print(var)

variavel = funcao('Valor que eu quero')
print(variavel)

def funcao1(var):
    print(var)

variavel1 = funcao1('Valor que eu quero')
if variavel1:
    print(variavel1)
else:
    print('Nenhum valor.')

def funcao2(var):
    return var  #Quando encontra um return, acaba o def e não executa as linhas sem sequencial do def
    print('Isso não será executado')

variavel2 = funcao2('Valor que eu quero')
if variavel2:
    print(variavel2)
else:
    print('Nenhum valor.')
