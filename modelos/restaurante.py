class Restaurante():
    restaurantes = []

    def __init__(self, nome, categoria): # Construtor (método especial)
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self): # Método especial
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(15)} | {'Status'}')
        for rest in Restaurante.restaurantes:
            print(f'{rest.nome.ljust(25)} | {rest.categoria.ljust(15)} | {rest.ativo}')

    @property # Modifica como um atributo é lido
    def ativo(self):
        return '▣' if self._ativo else '▢'


restaurante_praca = Restaurante('Praça Restaurante', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()
