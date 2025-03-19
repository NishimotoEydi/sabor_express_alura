from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praca', 'gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Jao', 8)
restaurante_praca.receber_avaliacao('Maria', 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()