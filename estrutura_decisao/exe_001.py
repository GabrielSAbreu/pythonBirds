'''Faça um Programa que peça dois números e imprima o maior deles. '''
from cabecalho import linha as l
l('_','Qual maior')

num_1 = int(input('Informe um número inteiro: '))

num_2 = int(input('Informe outro número inteiro: '))

if num_1 > num_2:
    print(f'{num_1} é o maior número informado')
else:
    print(f'{num_2} é o maior número informado')
