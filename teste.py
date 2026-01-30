import os
from modelos.restaurantes import Restaurante
from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebidas import Bebidas

restaurante_praca = Restaurante('Praça', 'Comida caseira')
bebida_suco = Bebidas('Suco de Laranja', 5.0, 'Suco natural de laranja', '300ml')
prato_feijoada = Prato('Feijoada', 25.0, 'Feijoada completa com arroz, farofa e couve', ['feijão preto', 'carne seca', 'linguiça', 'arroz', 'farofa', 'couve'])
bebida_suco.aplicar_desconto(0.1)
prato_feijoada.aplicar_desconto(0.1)
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_feijoada)


def exibir_cardapio(restaurante):
    print(f'Cardápio do restaurante {restaurante._nome}:')
    for item in restaurante._cardapio:
        print(f'- {item}')

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()