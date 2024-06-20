'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. '''

from cabecalho import linha as l

l('_',"Qual o genero")

genero = input('Informe seu genero (M/F): ').upper()

if genero == 'F':
    print('F - Feminino')
elif genero == 'M':
    print('M - Mascuino')
else:
    print('Resposta inválida')