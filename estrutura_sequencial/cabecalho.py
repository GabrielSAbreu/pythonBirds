def linha(char, nome_programa):
    '''Cria um cabeçalho para os programas
    >>> ---------------- retorna 1º parametro
    >>> nome programa    retorna 2º paramentro
    >>> ---------------- retorna 1º parametro
    '''
    print(char * 32)
    print(nome_programa)
    print(char *32)

if __name__ =="__main__":
    linha('-','Teste de nome')
    