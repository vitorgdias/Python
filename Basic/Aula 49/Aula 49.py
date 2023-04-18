while True:
    escolha = input('Deseja verificar um CPF [S] ou [N]? ')
    escolha = escolha.lower()
    if escolha == 's':
        cpf = input('Digite o seu CPF: ')
        comprimento = len(cpf)
        if not cpf.isnumeric() or comprimento != 11:
            print('Você digitou um cpf invalido')
        else:
            novo_cpf = cpf[:9]
            reverso = 10
            total = 0
            for index in range(19):
                if index > 8:
                    index -= 9
                total += int(novo_cpf[index]) * reverso

                reverso -= 1
                if reverso < 2:
                    reverso = 11
                    d = 11 - (total % 11)
                    if d > 9:
                        d = 0
                    total = 0
                    novo_cpf += str(d)
        if cpf == novo_cpf:
            print('Válido')
        else:
            print('Inválido')
    elif escolha == 'n':
        break
    else:
        print('Digite [S] ou [N]')
