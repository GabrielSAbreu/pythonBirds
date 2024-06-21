'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. '''

from cabecalho import linha
linha(nome_programa='Qual produto mais barato')

produto_1 = float(input('Informe o preço do 1º produto R$: '))
produto_2 = float(input('Informe o preço do 2º produto R$: '))
produto_3 = float(input('Informe o preço do 3º produto R$: '))

menor = float

if produto_1 < produto_2 and produto_2 < produto_3:
    menor = produto_1
elif produto_2 < produto_3:
    menor = produto_2
else:
    menor = produto_3

print(f'O produto mais barato é o  que custa R$ {menor:.2f}')