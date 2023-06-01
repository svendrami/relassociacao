class Emprego:
    # id: int
    # funcao: str
    # horario_inicio: str
    def __init__(self, id, funcao, horario_inicio):
        self.id = id
        self.funcao = funcao
        self.horario_inicio = horario_inicio

class Pessoa:
    # id: int
    # nome: str
    # email: str
    # emprego: Emprego

    def __init__(self, id, nome, email, emprego: Emprego):
        self.id = id
        self.nome = nome
        self.email = email
        self.emprego = emprego
#def main():
e = Emprego(1, 'dev python', '08:00am')
p = Pessoa(1, 'hugo', 'hu@gmail.com', e)
print(p.id, p.nome, p.email, p.emprego.funcao, p.emprego.horario_inicio)
    # print(p.id, p.nome, p.email, p.emprego) -- imprime a classe

#main()