'''Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''
class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    #Metodos
    def mudaValorLado():
        novoLado = float(input('Informe um novo valor para o lado:'))
        return novoLado

    def valorLado(lado):
        return lado
    
    def retornarLado_e_Area():
        pass

if __name__ == '__main__':

    forma = Quadrado(2)
    forma.valorLado(2)
    forma.mudaValorLado()