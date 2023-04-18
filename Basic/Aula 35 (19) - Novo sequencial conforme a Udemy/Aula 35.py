'''
While / Else
Contadores
Acumuladores
'''


c = 1
a = 1
while c <= 10:
    print(c, a)

    if c >5:
        break

    a = a + c
    c += 1
else:
    print('Cheguei no else')
print('Executas')
