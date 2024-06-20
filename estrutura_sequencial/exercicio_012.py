'''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58 '''

from estrutura_decisao.cabecalho import linha
linha('_'," Calculadora peso ideal")

altura = float(input('Informe sua altura em cm: '))

peso_ideal = 72.7 * (altura / 100) - 58

print(f'Com uma altura de {altura /100 } m , seu peso ideal é {peso_ideal:.2f} kg')