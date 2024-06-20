'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. '''
from cabecalho import linha
import math

linha('=','Calculadora quantidade tinta')

metros_quadrados = 200 #float(input('Informe a área a ser pintada em m²: '))
litros = metros_quadrados / 6

latas_18 = math.ceil(litros / 18)

galoes = math.ceil(litros / 3.6)

#calculo otimizado
n_de_latas = math.floor(litros / 18)
quantidade_latas = n_de_latas * 80
litros_faltantes = litros % 18
n_de_galoes = math.ceil(litros_faltantes / 3.6)
quantidade_galoes = n_de_galoes * 25
valor_total = quantidade_latas +  quantidade_galoes

print(f'Para pintar uma área de {metros_quadrados}m² você pode utilizar:')
print(f'{latas_18} lata(s) de 18 L = R${latas_18 * 80:.2f}')
print(f'{galoes} galoes de 3.6 L = R${galoes * 25:.2f}')
print(f'Você pode utilizar {n_de_latas} de 18 l + {n_de_galoes} de 3.6 l, no valor de R$ {valor_total}')