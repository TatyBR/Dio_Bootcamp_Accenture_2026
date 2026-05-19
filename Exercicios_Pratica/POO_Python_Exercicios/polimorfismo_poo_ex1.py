class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au Au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

# Função polimórfica — aceita qualquer Animal
# A função fazer_falar é polimórfica pois aceita qualquer objeto que seja uma especialização de Animal, 
# e cada um se comporta do seu jeito.
def fazer_falar(animal: Animal):
    print(animal.falar())


fazer_falar(Cachorro())
fazer_falar(Gato())
    

