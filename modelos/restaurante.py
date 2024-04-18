class Restaurante():
    def __init__(self, nome, categoria): # Construtor
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')
print(vars(restaurante_praca))
print(vars(restaurante_pizza))

'''
# Mostrando os atributos de uma Classe
print(dir(restaurante_praca))
# Mostra um dicionário com chaves e valores
print(vars(restaurante_praca))
'''