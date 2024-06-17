"""Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
notas = []
s = 0
for i in range(0,4):
    n = float(input(f'Informe a {i+1}ª notas:'))
    notas.append(n)
    s += n
m = s / 4
print(f'As notas informadas foram {notas} e a média é: {m:.2f}')
