class Restaurante():
    restaurantes = []

    def __init__(self, nome, categoria): # Construtor (método especial)
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self): # Método especial
        return f'{self._nome} | {self._categoria}'
    
    @classmethod # Informando que é um método da classe
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(15)} | {'Status'}')
        for rest in cls.restaurantes:
            print(f'{rest._nome.ljust(25)} | {rest._categoria.ljust(15)} | {rest.ativo}')

    @property # Modifica como um atributo é lido
    def ativo(self):
        return '▣' if self._ativo else '▢'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
