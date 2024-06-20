'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''
from estrutura_decisao.cabecalho import linha

linha('_','Calculadora salarial plus')
valor_hora = float(input('Informe quanto você ganha por hora: R$ '))
horas_trabalhadas = float(input('Informe as horas trbalhadas no mês: '))
salario_bruto = horas_trabalhadas * valor_hora
imposto_renda = salario_bruto * 11 / 100
inss = salario_bruto * 8 / 100
sindicato = salario_bruto * 5 / 100
descontos = salario_bruto - (inss + imposto_renda + sindicato)
salario_liquido = salario_bruto - descontos

print(f'+ Salário Bruto :   R$ {salario_bruto}')
print(f'- IR (11%) :        R$ {imposto_renda}')
print(f'- INSS (8%) :       R$ {inss}')
print(f'- Sindicato ( 5%) : R$ {sindicato}')
print(f'= Salário Liquido : R$ {salario_liquido:.2f}')



