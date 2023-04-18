logins = []
senhas = []
while True:
    temp1 = input('Selecione [L] para Login, [C] para Cadastro ou [S] para sair: ')
    temp1 = temp1.lower()
    if temp1 == 's':
        break
    elif temp1 == 'c':
        user = input('Digite um login com no mínimo 5 dígitos: ')
        luser = len(user)
        if luser < 5:
            print('Login inválido.')
            continue
        else:
            print(f'Login {user} aceito.')
            user = user.lower()
        senha = input('Digite uma senha numérica com no mínimo 8 caracteres: ')
        if not senha.isnumeric():
            print('Digite apenas números.')
            continue
        else:
            pass
        lsenha = len(senha)
        if lsenha < 8:
            print('A senha não atende ao requisito.')
        else:
            print('Senha criada com sucesso.')
        logins.append(user)
        senhas.append(senha)
    elif temp1 == 'l':
        log = input('Digite seu login: ')
        log = log.lower()
        senha = input('Digite sua senha: ')
        senha = senha.lower()
        if log not in logins:
            print('Login não cadastrado.')
            continue
        elif senha not in senhas:
            print('Senha incorreta.')
        else:
            print('Login feito com sucesso!')
            break
    else:
        print('Você não digitou uma opção válida.')
        continue
