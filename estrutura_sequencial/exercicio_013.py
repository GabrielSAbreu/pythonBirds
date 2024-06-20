'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 '''
from estrutura_decisao.cabecalho import linha
linha('_',"Peso ideal por genero")

h_cm = float(input('Informe sua altura em cm: '))
genero = input('Informe  seu genero (M / F): ').lower()
h_m = h_cm /100
if genero == 'm':
    peso_ideal = 72.7 * (h_m) - 58
    print(f'Para uma altura de {h_m} do genero masculino o peso ideal é: {peso_ideal:.2f} KG')
else:
    peso_ideal = 62.1 * (h_m) - 44.7
    print(f'Para uma altura de {h_m} m do genero feminino o peso ideal é: {peso_ideal:.2f} KG')

