'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. '''
from cabecalho import linha
linha('=','Calculadora quantidade tinta')

metros_quadrados = float(input('Informe a área a ser pintada em m²: '))
litros = metros_quadrados / 6

latas_18 = litros / 18
if latas_18 < 1:
    latas_18 = 1
galoes = litros / 3.6
if galoes < 1:
    galoes = 1

print(f'Para pintar uma área de {metros_quadrados}m² você pode utilizar:')
print(f'{round(latas_18)} lata(s) de 18 L = R${latas_18 * 80:.2f}')
print(f'{round(galoes)} galoes de 3.6 L = R${galoes * 25:.2f}')