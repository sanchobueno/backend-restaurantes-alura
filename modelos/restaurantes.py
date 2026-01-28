class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = True
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {"Ativo" if self.ativo else "Inativo"}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            status = 'Ativo' if restaurante.ativo else 'Inativo'
            print(f'- {restaurante.nome.ljust(20)} | - {restaurante.categoria.ljust(20)} | {status}')
    
restaurante_praca = Restaurante('Praça', 'Comida caseira')
restaurante_pizza = Restaurante('Pizza', 'Comida italiana')

Restaurante.listar_restaurantes()

