'''Faça um Programa que leia três números e mostre-os em ordem decrescente. '''

n1 = 2
n2 = 1
n3 = 3
'''podemos ter os seguintes cenários:
n1 > n2 > n3
n1 > n3 > n2
n2 n3 n1
n2 n1 n3
n3 n2 n1
n3 n1 n2
'''
if n1 > n2 > n3:#A
    print(n1,n2,n3)
    print('A')
elif n1 > n2 < n3 < n1:#B
    print(n1,n3,n2)
    print('B')
elif n1 < n2 > n3 > n1:#C
    print(n2,n3,n1)
    print('C')
elif n1 < n2 > n3 < n1:#D
    print(n2,n1,n3)
    print('D')
elif n1 < n2 < n3:#E
    print(n3,n2,n1)
    print('E')
else:
    print(n3,n1,n2)
    print('F')
