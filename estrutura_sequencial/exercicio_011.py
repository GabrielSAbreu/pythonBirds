'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo. '''
from cabecalho import linha
linha('*','Calculando números inteiros e reais ')

num_1 = int(input('Informe o 1º número inteiro: '))
num_2 = int(input('Informe o 2º número inteiro: '))
num_3 = float(input('Informe um número real (separado por ponto ex: 2.5): '))

produto = (num_1 * 2) * (num_2 / 2)
soma = (num_1 * 3) + num_3

print(f' o produto de {num_1} com metade de {num_2} é: {produto}')
print(f' A soma do triplo de {num_1} com o {num_3} é: {soma}')
print(f' {num_3} elevado ao cubo é: {num_3 ** 3}')