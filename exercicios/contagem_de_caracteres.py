def contar_caracter(s):
    ''' função para contagem de caracter de uma string
        EX:
        >>> contar_caracter('ana')
        a: 2
        n: 1
    '''
    caracteres_ordenados = sorted(s.lower())
    
    caracter_anterior = caracteres_ordenados[0]
    contagem = 1
    

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior = caracter
            contagem = 1
    print(f'{caracter_anterior}: {contagem}')

if __name__ == '__main__':
    contar_caracter('BaNana')
    print('')
    contar_caracter('Paralelepipedo')