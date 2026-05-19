class Pessoa:
    def __init__(self, nome, ano_nascim):
        self.nome = nome
        self._ano_nascim = ano_nascim
        
    @property
    def idade(self):
        _ano_atual = 2026
        return _ano_atual - self._ano_nascim


pessoa = Pessoa("Lucas", 2015)

print(f"Nome: {pessoa.nome} - Idade: {pessoa.idade} anos")