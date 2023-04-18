user = input("Digite seu usuário: ")
qtd = len(user)
if qtd<6:
    print("Digite pelo menos 6 caracteres")
else:
    print('Cadastro concluido')

str1 = input('Digite algo')
str2 = input('Digite algo')

print(f'A qtd de caracteres digitados foi {len(str1) + len(str2)}')
