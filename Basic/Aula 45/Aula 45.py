# Operador ternário em Python

logged_user = False

if logged_user:  #mesma coisa que 'if logged_user == True:'
    msg = 'Usuário logado'
else:
    msg = 'Usuário precisa logar'

print(msg)

#Com operador ternário
logged_user = True
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar'
print(msg)

idade = 18
if idade >= 18:
    print('Pode acessar')
else:
    print('Não pode acessa')
idade = input('Qual sua idade? ')
if not idade.isnumeric():
    print('Digite numeros')
else:
    idade = int(idade)
    emaior = (idade>=18)
    msg = 'Pode acessar' if emaior else 'Não pode acessar'
    print(msg)
