#  positivos [012345678]
texto = 'Python_s2'
print(texto[2])

url = 'www.google.com.br/'

print(url[:-1])  #retirou a / do final da url
#  Negativos  -[987654321]

ns = texto[2:6]  #vai até o caractere 5
print(ns)

ns1 = texto[-1]
print(ns1)

ns2 = texto[-9:-3]
print(ns2)

nst = texto[:6]
print(nst)

nst1 = texto[7:]
print(nst1)

#Pular caractere
novo = texto[0:6:2]  #do 0 ao 5 pulando de 2 em 2
print(novo)

novo1 = texto[0::3]  #até o final pulando de 3 em 3
print(novo1)