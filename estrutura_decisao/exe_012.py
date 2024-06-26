'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220. '''

from cabecalho import linha
linha(nome_programa='Folha de pagamento')

#valor da sua hora
valor_hora = float(input('Informe o valor da sua hora trabalhada R$: '))

#quantidade de horas trabalhadas
hora_trabalhadas = float(input('Informe a quantidade de horas trabalhadas no mês: '))

salario_bruto = valor_hora * hora_trabalhadas

if salario_bruto <= 900:
    ir = 0
elif 900 > salario_bruto <= 1500:
    ir = salario_bruto * 5 / 100
elif 1500 > salario_bruto <= 2500:
    ir = salario_bruto * 10 / 100
else:
    ir = salario_bruto * 20 / 100

fgts = salario_bruto * 11 / 100

sindicato = salario_bruto * 3 / 100

inss = salario_bruto * 10 / 100

descontos = ir + sindicato + inss

salario_liquido = salario_bruto - descontos

linha(nome_programa='Contra cheque')

print(f'Salário Bruto: ({valor_hora} * {hora_trabalhadas})        : R$ {salario_bruto}')
print(f'(-) IR (5%)                     : R$ {ir}')
print(f'(-) INSS ( 10%)                 : R$ { inss }')
print(f'(-) Sindicato (3%)              : R$ { sindicato }')
print(f'FGTS (11%)                      : R${  fgts} ')
print(f'Total de descontos              : R${  descontos}')
print(f'Salário Liquido                 : R${  salario_liquido}')
        
        
        
        
        