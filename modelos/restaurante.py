class Restaurante():
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

# Mostrando os atributos de uma Classe
print(dir(restaurante_praca))
# Mostra um dicionário com chaves e valores
print(vars(restaurante_praca))