'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante. '''

from cabecalho import linha

linha('_','Vogal ou consoante')

vogais = ['A','E','I','O','U']

letra = input('Informe uma letra: ').upper()

if letra in vogais:
    print(f'{letra} é uma vogal')
else:
    print(f'{letra} é uma cosoante')