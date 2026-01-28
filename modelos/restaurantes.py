class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {"Ativo" if self.ativo else "Inativo"}'

    @classmethod
    def listar_restaurantes(cls):
        print()
        print(f'{"Restaurante".ljust(27)} | {"Categoria".ljust(27)} | Status\n')
        for restaurante in cls.restaurantes:
            print(f'- {restaurante._nome.ljust(25)} | - {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'
    
    def alternar_status(self):
        self._ativo = not self._ativo
        return self.ativo
    
    
restaurante_praca = Restaurante('Praça', 'Comida caseira')
restaurante_praca.alternar_status()
restaurante_pizza = Restaurante('Pizza', 'Comida italiana')
restaurante_burger = Restaurante('Burger', 'Comida americana')

Restaurante.listar_restaurantes()

