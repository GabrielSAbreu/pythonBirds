'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento'''

from cabecalho import linha
linha(nome_programa='Calculadora salário Tabajara')

salario = float(input('Informe o salário R$: '))

if salario <= 280:
    percentual = 20
    aumento = salario * percentual / 100
    novo_salario = salario + aumento
elif 280 < salario <= 700:
    percentual = 15
    aumento = salario * percentual / 100
    novo_salario = salario + aumento
elif 700 < salario <= 1500:
    percentual = 10
    aumento = salario * percentual / 100
    novo_salario = salario + aumento
else:
    percentual = 5
    aumento = salario * percentual / 100
    novo_salario = salario + aumento

linha(nome_programa='Salario reajustado')
print(f'Salario antes do reajuste R$: {salario}')
print(f'Percenual de aumento (%): {percentual}')
print(f'Valor do aumento R$: {aumento}')
print(f'Salario apos reajuste R$: {novo_salario}')

