h = input('Digite um horário entre 0 e 23 horas: ')
if h.isdigit():
    h=int(h)
    if h>=0 and h<=11:
        print('Bom dia')
    elif h>=12 and h<=17:
        print('Boa tarde')
    elif h>=18 and h<=23:
        print('Boa noite')
    elif h>23:
        print('O horário deve estar entre 0 e 23')
else:
    print('Você não digitou um valor válido')