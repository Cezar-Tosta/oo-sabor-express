from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.00, 'Grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Pãozinho', 2.00, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

sobremesa_doce = Sobremesa('Doce de leite', 2.00, 'Caseiro', 'Pequeno')
restaurante_praca.adicionar_no_cardapio(sobremesa_doce)
sobremesa_doce.aplicar_desconto()

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()