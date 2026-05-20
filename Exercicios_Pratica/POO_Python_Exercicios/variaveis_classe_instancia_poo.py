class Estudante:
    # variável de classe: logo após class/ única para TODOS os objetos
    escola = "DIO"

    def __init__(self, nome, matricula):
        # variáveis de instância: única por objeto
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self) -> str:
        return f"{self.nome} ({self.matricula}) - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno1 = Estudante("Lucas", 11223344)
aluno2 = Estudante("Taíta", 55667788)
mostrar_valores(aluno1, aluno2)

# variável de classe:
Estudante.escola = "Python"
# variável de instância:
aluno1.matricula = 9900112233
aluno3 = Estudante("Paula", 77665544)
mostrar_valores(aluno1, aluno2, aluno3)