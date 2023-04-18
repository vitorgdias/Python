l1 = [1,2,3]
l2 = [4,5,6]
print(l1)
print(l2)
l3 = l1 + l2
print(l3)

l1.extend(l2)
print (l1)
l1.extend('a')  #Extende a lista
print(l1)

l2.append('b')  #insere no final da lista
print(l2)
print(l2[3])

l2.insert(0, 'Banana')  #Insere no indice desejado
print(l2)
l2.pop()
print(l2)

l3 = [0,1,2,3,4,5,6,7,8,9]
print(l3)
del(l3[3:5])
print(l3)

l4 = [0,1,2,3,4,5,6,7,8,9]
print(l4)
l4.insert(0, 'banana')
del(l4[0])
print(l4)
print(max(l4))
print(min(l4))
