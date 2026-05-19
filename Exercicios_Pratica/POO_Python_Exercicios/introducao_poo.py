# Definindo classe Bicicleta

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Plim... plim...")
    
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!!")

    def correr(self):
        print("Vrrruumm....")
    
    # Não é uma boa prática(pois os atributos são acessíveis publicamente!):
    # def get_cor(self):
        # return self.cor
    
    # Para exibir a instância/ Representação para o usuário
    # def __str__(self):
        # return f"Bicicleta - Cor: {self.cor} - Modelo: {self.modelo} - Ano: {self.ano} - Valor:{self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"
    
# bicicleta1 = Bicicleta("vermelha", "calo1", 2002, 600.50)
# bicicleta1.buzinar()
# bicicleta1.parar()
# bicicleta1.correr()
# print(f"Bicicleta 1: Cor {bicicleta1.cor}, Modelo {bicicleta1.modelo}, Ano {bicicleta1.ano} e Valor R${bicicleta1.valor}")

bicicleta2 = Bicicleta("verde", "monark", 2000, 300.00)
bicicleta2.buzinar()
# Bicicleta.buzinar(bicicleta2)
# print(bicicleta2.get_cor())
# Atribuito acessível publicamente
print(bicicleta2.cor)   # também funciona: bicicleta2.cor

