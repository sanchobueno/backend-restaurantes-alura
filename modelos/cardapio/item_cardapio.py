from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco, descricao):
        self._nome = nome
        self._preco = preco
        self._descricao = descricao

    @abstractmethod
    def aplicar_desconto(self, desconto):
        pass