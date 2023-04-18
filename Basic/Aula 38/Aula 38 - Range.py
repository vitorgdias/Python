'''
l1 = range(1,10)
print(l1)

l2 = list(range(1,10))
print(l2)

l3 = list(range(0,100,8))
print(l3)
for valor in l3:
    print(valor)

l4 = [0,1,2,3,4,5,6,7,8,9]
soma = 0
for valor in l4:
    soma = soma + valor
    print(f'{soma} + {valor} = {soma}')

l5 = ['Sting', True, 10, -25.5]
for elem in l5:
    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')
'''
secreto = 'perfume'
digitadas = []
chances = 3
while True:
    if chances <= 0:
        print('Você perdeu!')
        break
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Isso não vale, digite apenas uma letra')
        continue
    digitadas.append(letra)
    if letra in secreto:
        print(f'Uhuul, a letra {letra} existe na palavra secreta')
    else:
        print(f'Aff: a letra {letra} não existe na palavra secreta')
        digitadas.pop()
    secreto_temporário = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporário += letra_secreta
        else:
         secreto_temporário += '*'
    if secreto_temporário == secreto:
        print(f'Que legal, você ganhou!! A palavra era {secreto_temporário}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporário}')

    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')
    print()

