# For / Else

variavel = ['Vitor', 'João','Maria']

for valor in variavel:
    print(valor)
    continue
    print(valor)

for valor in variavel:
    print(valor)
    break
    print(valor)

for valor in variavel:
    if valor.startswith('V'):
        print('Começa com V')
    else:
        print('Não começa com V', valor)

v = False
for valor in variavel:
    if valor.startswith('V'):
        v = True
if v:
    print('Existe uma palavra que começa com V')
else:
    print('Não existe nenhuma palavra que começa com V')

for valor in variavel:
    if valor.lower().startswith('v'):
        v = True
if v:
    print('Existe uma palavra que começa com V')
else:
    print('Não existe nenhuma palavra que começa com V')

for valor in variavel:
    if valor.lower().startswith('v'):
        v = True
        break  #podemos usar continue ou pass também, porém irá executar o else em seguida
else:
    print('Não existe nenhuma palavra que começa com V')