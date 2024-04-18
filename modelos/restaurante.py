class Restaurante():
    restaurantes = []

    def __init__(self, nome, categoria): # Construtor (método especial)
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self): # Método especial
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for rest in Restaurante.restaurantes:
            print(f'{rest.nome} | {rest.categoria} | {rest.ativo}')


restaurante_praca = Restaurante('Praça Restaurante', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()
