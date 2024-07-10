'''Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        
    #Declaração dos métodos

    def trocaCor(self):
        novaCor = input('Informe uma nova cor:')
        return novaCor

    def mostraCor(self):
        print(f'A antiga cor era {self.cor} agora a nova cor é {bola.trocaCor()}')
    
bola  = Bola('rosa' , 15 , 'plastico')

bola.mostraCor()