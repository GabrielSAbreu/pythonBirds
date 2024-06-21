'''Faça um Programa que leia três números e mostre o maior e o menor deles. '''

from cabecalho import linha

linha(nome_programa='Maior e menor')

num_1 = int(input('Informe o 1º número: '))
num_2 = int(input('Informe o 2º número: '))
num_3 = int(input('Informe o 3º número: '))

menor = int
maior = int
#Verifica qual é maior
if num_1 > num_2 and num_2 > num_3:
    maior = num_1
elif num_2 > num_3 and num_3 > num_1:
    maior = num_2
else:
    maior = num_3
#Verifica qual é menor
if num_1 < num_2 and num_2 < num_3:
    menor = num_1
elif num_2 < num_3 and num_3 < num_1:
    menor = num_2
else:
    menor = num_3

print(f'O maior número informado foi {maior} e o menor número foi {menor}')