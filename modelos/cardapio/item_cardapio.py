# Essa vai ser a classe pai (p. ex: bebida e prato)

from abc import ABC, abstractmethod # Importando o necessário para criar uma classe abstrata

class ItemCardapio(ABC):
    def __init__(self,nome,preco):
        self._nome = nome #  O uso de _ antes de 'nome' é uma convenção em Python para indicar que essas variáveis são "privadas" ou "protegidas".
        self._preco = preco
    
    @abstractmethod # Todas as classes derivadas precisam = POLIMORFISMO
    def aplicar_desconto(self):
        pass
