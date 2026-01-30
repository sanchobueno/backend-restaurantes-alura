from modelos.cardapio.item_cardapio import ItemCardapio

class Bebidas(ItemCardapio):
    def __init__(self, nome, preco, descricao, tamanho):
        super().__init__(nome, preco, descricao)
        self.tamanho = tamanho

    def __str__(self):
        return self._nome + ' - ' + str(self._preco) + ' - ' + self._descricao + ' - ' + self.tamanho
    
    def aplicar_desconto(self, desconto):
        self._preco -= self._preco * desconto
        return self._preco