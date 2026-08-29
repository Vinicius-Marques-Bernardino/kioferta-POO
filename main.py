from dominio.produto import Produto
from dominio.mercado import Mercado
from dominio.oferta import Oferta


def main():
    mercados = [
        Mercado(1, "Guanabara", 80, 90),
        Mercado(2, "Valverde's Market", 190, -30),
        Mercado(3, "Max da Galera", 120, 40)
    ]

    produtos = [
        Produto(12, 'Delicia' , 60.5),
        Produto(20, 'Carioquinha' , 2.34),
        Produto(4, 'Quatro Corações', 398.45)
    ]
    
    print(mercados[1].mostra_mercado())

    for produto in produtos:
        print(f'{produto.id}\t {produto._nome} - R${produto._preco}')


if __name__ == '__main__':
   main()




