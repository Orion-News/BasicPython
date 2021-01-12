class Carro(object):
    
    def __init__(self, caminho): 
        self.caminho = caminho

    def andar():
        print('Andando pela', self.caminho)

class Fusca(Carro):

    def __init__(self, caminho):
        self.caminho = caminho

    def correr(self):
        self.caminho = 'pista'
        super(Fusca, self).andar()


""" sobrescrever method in class pai --- o tal do polimorfismo --- """

class Ferrari(Carro):
    
    def __init__(self, caminho): 
        self.caminho = caminho

    def andar():
        print('correndo muito')
