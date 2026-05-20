class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    # método de classe: acesso ao contexto da classe
    @classmethod
    def criar_apartir_nascimento(cls, ano, mes, dia, nome):
        idade = 2026 - ano
        return cls(nome, idade)
    
    # método estático: não preciso de contexto, nem de classe e nem da instância objeto
    @staticmethod
    def maior_idade(idade):
        return idade >= 18


p = Pessoa("lucas", 10)
print(p.nome, p.idade)

p2 = Pessoa.criar_apartir_nascimento(2015, 7, 21, "Lucas")
print(p2.nome, p2.idade)

print(Pessoa.maior_idade(19))
print(Pessoa.maior_idade(5))
