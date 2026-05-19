# _saldo: variável privada/ só deve ser acessada no escopo da classe.
# nro_agencia: variável pública.
# Acesso a _saldo fora da classe funciona/ mas por boas práticas se está declarada como privada, não pode ser acessada dessa forma: conta._saldo
# Forma correta de acessar variável privada: utilizar método.

class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ---
        self._saldo += valor

    def sacar(self, valor):
        # ---
        self._saldo -= valor
    
    def mostrar_saldo(self):
        # ---
        return self._saldo

conta = Conta("00001", 100)
conta.depositar(100)

# print(conta._saldo)

print(f"Saldo atual da conta: R$ {conta.mostrar_saldo()} - Agência:{conta.nro_agencia}")