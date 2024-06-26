class Pessoa:
    def cumpruimentar(self):
        return 'Olá'
    

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumpruimentar(p))
    print(p.cumpruimentar())