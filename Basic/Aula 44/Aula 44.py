
x = 10
y = 'Luiz'
#Inverter as variáveis
z = x
x = y
y = z
print(f'x={x} e y={y}')

# Em python pode-se usar:
z = 10
v = 'Luiz'

z, v = v, z
print(z, v)

x1 = 10
y1 = 'Luiz'
z1 = 'Vitor'

x1, y1, z1 = z1, x1, y1
print(x1, y1, z1)