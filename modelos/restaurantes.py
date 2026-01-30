from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
   
    restaurantes = []
   
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {"Ativo" if self.ativo else "Inativo"}'

    @classmethod
    def listar_restaurantes(cls):
        print()
        print(f'{"Restaurante".ljust(27)} | {"Categoria".ljust(27)} | {"Avaliação".ljust(27)} | Status\n')
        for restaurante in cls.restaurantes:
            print(f'- {restaurante._nome.ljust(25)} | - {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(27)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'
    
    def alternar_status(self):
        self._ativo = not self._ativo
        return self.ativo
    
    def receber_avaliacao(self, cliente, nota, comentario=''):
        if nota < 0 or nota > 5:
            raise ValueError('A nota deve ser entre 0 e 5.')
        avaliacao = Avaliacao(cliente, nota, comentario)
        self._avaliacao.append(avaliacao)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}:\n')
        for i,item in enumerate(self._cardapio, start=1):
            mensagem = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item._descricao}'
            print(mensagem)
            if hasattr(item, 'ingredientes'):
                print(f'   Ingredientes: {", ".join(item.ingredientes)}')
            if hasattr(item, 'tamanho'):
                print(f'   Tamanho: {item.tamanho}')

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'sem avaliações'
        total = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media = round(total / len(self._avaliacao), 1)
        return media
    
