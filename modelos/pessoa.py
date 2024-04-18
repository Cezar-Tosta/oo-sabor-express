class Pessoa():
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome} tem {self.idade} anos e é {self.profissao}.' if self.profissao else f'{self.nome} tem {self.idade} anos.'
    
    def aniversario(self):
        self.idade += 1
    
    @property # Determina a forma como o atributo será mostrado
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}. Trabalho como {self.profissao}!'
        else:
            return f'Olá, sou {self.nome}!'

pessoa1 = Pessoa('Cezar', 39, 'militar')
pessoa2 = Pessoa('Emilly', 15)
print(pessoa1)
print(pessoa2)
pessoa1.aniversario()
print(pessoa1.saudacao)
print(pessoa2.saudacao)