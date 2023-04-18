'''
For in
Iterando strings com for

texto = 'Python'
c = 0
while c < len(texto):
    print(texto[c])
    c += 1
'''
texto = 'Python'

for letra in texto:
    print(letra)

for n, letra in enumerate(texto):
    print(n, letra)
