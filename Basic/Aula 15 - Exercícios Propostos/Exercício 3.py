n = input('Digite seu nome: ')
t = len(n)
if t<=4:
    print('Seu nome é curto')
elif t>= 5 and t<=6:
    print('Seu nome é normal')
elif t>6:
    print('Seu nome é muito grande')
