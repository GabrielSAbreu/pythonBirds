'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. '''

from cabecalho import linha
linha('=','Calculadora quantidade tinta')

metros_quadrados = float(input('Informe a área a ser pintada em m²: '))
litros = metros_quadrados / 3

if litros <= 18:
    print(f'você precisa de 1 lata de 18 L de tinta no valor de R$80.00')
else:
    quantidade_latas = litros / 18
    print(f'Você precisa de {round(quantidade_latas)} latas de 18 L e o valor é R$ {quantidade_latas * 80:.2f}')