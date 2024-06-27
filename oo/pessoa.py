class Pessoa:
    def __init__(self, *filhos,  nome = None, idade = 38):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
       
    def cumprimentar(self):
        return 'Olá'
    

if __name__ == '__main__':
    aurora = Pessoa(nome='Aurora')
    gabriel = Pessoa(aurora, nome = 'Gabriel')
    print(Pessoa.cumprimentar(gabriel))
    print(gabriel.cumprimentar())
    print(gabriel.nome)
    print(gabriel.idade)
    for filho in gabriel.filhos:
        print(filho.nome)

'''if __name__ == '__main__':
    aurora = Pessoa(nome='Aurora')
    gabriel = Pessoa(aurora, nome='Gabriel')
    print(Pessoa.cumprimentar(gabriel))
    print(gabriel.cumprimentar())
    print(gabriel.nome)
    print(gabriel.idade)
    for filho in gabriel.filhos:
        print(filho.nome)'''
