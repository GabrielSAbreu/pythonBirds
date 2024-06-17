'''Faça um Programa que calcule a área de um quadrado, 
em seguida mostre o dobro desta área para o usuário.
'''
lado =float(input('Informe o lado do quadrado: '))

area = lado ** 2
dobro = area * 2

print(f'A area de um quadrdo de lado {lado} é: {area:.2f} ')
print(f'O dobro de uma area {area} é: {dobro}')