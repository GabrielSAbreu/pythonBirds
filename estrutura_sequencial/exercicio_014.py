'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário 
de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento 
de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
 Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da 
 multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

'''
from estrutura_decisao.cabecalho import linha
linha('_',"Calculadora de multa")

peso = float(input('Informe o peso em kg: '))

if peso > 50:
    excedente = peso - 50
    multa = excedente * 4
    print(f'Você possui {excedente}kg a mais que o permitido, e deve pagar uma multa no valor de R${multa}')
else:
    print(f'O peso total é {peso} kg e não ultrapassa o limite de 50kg')