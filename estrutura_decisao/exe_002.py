'''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. '''
numero = int(input('Informe um número inteiro (positivo ou negativo): '))

if numero < 0:
    print(f'{numero} é negativo')
else:
    print(f'{numero} é positivo')