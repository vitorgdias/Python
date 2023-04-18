#Função range(start=0, stop, step=1)

for n in range(10):
    print(n)

for n in range(5, 10):
    print(n)

for n in range(20, 10, -1):
    print(n)

for n in range(100):
    if n % 8 == 0:
        print(n)

texto = 'Phyton'
ns = ''
for letra in texto:
    if letra == 't':
        continue
        ns = ns + letra.upper()
    elif letra == 'h':
        ns += letra.upper()
        break
    else:
        ns += letra
print(ns)
