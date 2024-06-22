'''Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", 
conforme o caso.'''

from cabecalho import linha
linha(nome_programa='Turno de estudo')

turno = input('Informe qual turno você estuda (M-matutino ou V-Vespertino ou N- Noturno): ').upper()

if turno == 'M':
    print('M-matutino')
elif turno == 'V':
    print('V-Vespertino')
elif turno == 'N':
    print('N-Noturno')
else:
    print('Valor inválido')