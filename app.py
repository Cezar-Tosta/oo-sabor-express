from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_praca.receber_avaliacao('Cezar', 10)
restaurante_praca.receber_avaliacao('Emilly', 9)
restaurante_praca.receber_avaliacao('Daiany', 7)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()