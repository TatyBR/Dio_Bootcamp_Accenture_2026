class Forma:
    def area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado **2

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return 3.1 * self.raio ** 2

class Calculadora:
    def calcular_area(self, forma: Forma): # referencia o tipo abstrato
        return forma.area()                # comportamento muda conforme o objeto recebido

calc = Calculadora()

lado_quadr = int(input("Digite a quantidade de lados do quadrado:"))
raio = int(input("Digite o raio do circulo:"))

area_quadr = calc.calcular_area(Quadrado(lado_quadr))
area_circ = round(calc.calcular_area(Circulo(raio)),2)

print(f"A área do quadrado é: {area_quadr}.")
print(f"A área do círculo é: {area_circ}.")