class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.nome= nome
        self.idade= idade

    def cumprimentar(self):
        return f'olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Alessandra')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    p.nome = 'Murilo'
    print(p.nome)
    print(p.idade)



    