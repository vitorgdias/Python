#  Indices
#        0123456789.......................33
frase = 'O rato roeu a roupa do rei de roma'  #Valores iteráveis
tamanho = len(frase)
contador = 0
ns = ''

'''
while contador < tamanho:
    #  print(frase[contador], contador)
    ns += frase[contador]
    contador += 1
    print(ns)
'''
usuario = input('Qual letra deseja colocar maiuscula? ')
while contador < tamanho:  #Iteração (iterando), percorre cada um dos elementos da string.
    letra = frase[contador]
    if letra == usuario:
        ns += usuario.upper()
    else:
       ns += letra
    contador += 1
print(ns)
