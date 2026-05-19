# @property: Transforma o método x em uma propriedade
# É possível acessar o método como um simples atributo foo.x, sem precisar usar parênteses foo.x()

class Foo:
    def __init__(self, x=None):
        self._x = x
    
    @property
    def x(self):
        return self._x or 0
    
    @x.setter   # criada para que seja possíel alterar o valor de x
    def x(self, value):
        self._x += value
    
    @x.deleter
    def x(self):
        self._x = -1
    

foo = Foo(10) # Cria um objeto Foo passando x=10
print(foo.x)  # Acessa a propriedade x → imprime 10

del foo.x
print(foo.x)

foo.x = 10
print(foo.x)

