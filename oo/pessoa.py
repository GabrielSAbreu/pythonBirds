class Pessoa:
    def __init__(self, nome = None, idade = 38):
        self.nome = nome
        self.idade = idade
       
    def cumprimentar(self):
        return 'Olá'
    

if __name__ == '__main__':
    p = Pessoa('Gabriel', 40)
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)