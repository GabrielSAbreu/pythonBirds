'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. '''
from estrutura_sequencial.cabecalho import linha

linha('#')
print('Calculadora salário')
linha('#')
valor_hora = float(input('Informe quanto você recebe por hora: R$'))
total_hora= float(input('Informe o total de horas que você trabalhou no mês: '))
salario = valor_hora * total_hora

print(f'Você trabalhou {total_hora} horas, recebendo R${valor_hora} por hora trabalhada.Seu salário é R${salario}')