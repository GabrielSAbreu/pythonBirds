'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

    C = 5 * ((F-32) / 9). '''

from cabecalho import linha
linha('#','Conversor F para C')

f = float(input('Informe a temperatura em Fahrenheit: '))
c = 5 *((f - 32) / 9)

print(f'{f} F equivalem a {c:.1f} C')