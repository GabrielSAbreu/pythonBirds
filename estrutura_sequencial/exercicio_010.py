'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
C = 5 * ((F-32) / 9) '''

from estrutura_decisao.cabecalho import linha
linha('_', " Conversor C para F")

c = float(input('Informe a temperatura em graus C: '))
f = c * 9 / 5 + 32

print(f'{c}ºC equivalem a {f}F')