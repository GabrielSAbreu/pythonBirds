'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez. '''

from cabecalho import linha

linha(nome_programa='Media aluno')

nota_1 = float(input('Informe a 1ª nota: '))
nota_2 = float(input('Informe a 2ª nota: '))

media = (nota_1 + nota_2) / 2

if media == 10:
    print(f' A média é {media} = Aprovado com Distinção')
elif media >= 7 and media < 10:
    print(f' A média é {media} = Aprovado')
else:
    print(f' A média é {media} = Reprovado')

