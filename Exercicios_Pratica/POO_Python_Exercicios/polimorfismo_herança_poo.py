class Passaro:
    def voar(self):
        print("Voando....")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa...")

# EXEMPLO RUIM do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")

def plano_voo(obj):
    obj.voar()

animal1 = Pardal()
animal2 = Avestruz()

plano_voo(animal1)
plano_voo(animal2)
plano_voo(Aviao())