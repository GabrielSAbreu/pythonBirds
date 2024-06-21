'''Faça um Programa que leia três números e mostre o maior deles'''

from cabecalho import linha
linha(nome_programa='Qual o maior número')

num_1= int(input('Informe o 1º número: '))
num_2= int(input('Informe o 2º número: '))
num_3= int(input('Informe o 3º número: '))



if num_1 > num_2 and num_1 > num_3:
    print(f'{num_1} foi o maior número informado')

elif num_2 > num_3:

    print(f'{num_2} foi o maior número informado')

else:
    print(f'{num_3} foi o maior número informado')

