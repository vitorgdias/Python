'''
n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')

#  isnumeric, isdigit ou isdecimal

print(n1.isnumeric())
print(n2.isnumeric())
'''
#  isnumeric verifica se há número positivos na string, então retorna true.

n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')

if n1.isdigit() and n2.isdigit():
    n1 = int(n1)
    n2 = int(n2)
    print(n1+n2)
else:
    print("Valor inválido")
