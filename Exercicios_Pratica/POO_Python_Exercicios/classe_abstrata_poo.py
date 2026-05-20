# método abstrato: não tem um "corpo" e todas as suas classes filhas tem que implementar.
# Uma vez tendo o método abstrato, a classe se torna abstrata e ela não pode mais ser instanciada diretamente.

from abc import ABC, abstractmethod, abstractproperty 

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):    # contrato
        pass

    @abstractmethod
    def desligar(self): # contrato
        pass

    # Forçando uma propriedade
    @property
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")
    
    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"
    


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando Ar Condicionado...")
        print("Ligado!")
    
    def desligar(self):
        print("Desligando Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"



controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)

