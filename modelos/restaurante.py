class Restaurante():
    def __init__(self, nome, categoria): # Construtor (método especial)
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self): # Método especial
        return f'{self.nome} | {self.categoria}'

restaurante_praca = Restaurante('Praça Restaurante', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')
print(vars(restaurante_praca))
print(vars(restaurante_pizza))
print(restaurante_pizza)
print(restaurante_praca)

'''
# Mostrando os atributos de uma Classe
print(dir(restaurante_praca))
# Mostra um dicionário com chaves e valores
print(vars(restaurante_praca))
'''