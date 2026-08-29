from dominio.produto import Produto

class Mercado:
    produtos = []
    def __init__(self, id, nome, lat, long):
        self.id = id
        self.nome = nome
        self.lat = lat
        self.long = long

    def add_prod(self, produto: Produto):
        self.produtos.append(produto)

    def mostra_mercado(self):
        return f'Bem-vindo ao mercado {self.nome}'