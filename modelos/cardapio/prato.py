from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao, ingredientes):
        super().__init__(nome, preco, descricao)
        self.ingredientes = ingredientes

    def __str__(self):
        return self._nome + ' - ' + str(self._preco) + ' - ' + self._descricao + ' - ' + ', '.join(self.ingredientes)
    
    def aplicar_desconto(self, desconto):
        self._preco -= self._preco * desconto
        return self._preco