class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# nro_patas da classe base nas outras classes é substituido por **kw
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        # chamar construtor pai:
        super().__init__(**kw)
    
class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        # chamar construtor pai:
        super().__init__(**kw)

class Gato(Mamifero):
    pass

class FalarMixin:
    def falar(self):
        return "Olá, Olá, Olá"

class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        
        # Ordem de resolução pelo Python:
        # print(Ornitorrinco.__mro__)
        # print(Ornitorrinco.mro())
        
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)
    
# gato = Gato(nro_patas=4, cor_pelo ="preto")
# print(gato)

Orni = Ornitorrinco(nro_patas=2, cor_pelo="Vermelho", cor_bico="laranja")
print(Orni)
print(Orni.falar())