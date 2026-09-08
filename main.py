from dominio.produto import Produto
from dominio.mercado import Mercado
from dominio.oferta import Oferta
from dominio.contribuidor import Contribuidor
from dominio.moderador import Moderador
from dominio.visitante import Visitante




def main():
    ...
    usuarios = [
        Contribuidor()
    ]

if __name__ == '__main__':
   main()


#TIPOS DE RELACIONAMENTO
#ASSOCIAÇÃO - conhece - Um objeto guarda o outro. Independentes - linha simples
#AGREGAÇÃO - tem, mas não é dono - Um reúne os outros, que existem sem ele - losango vázio
#COMPOSIÇÃO - é dono - a parte não existe sem o todo - losango preenchido
#DEPENDÊNCIA - usa de passagem - só parâmetro de método. Não fica guardado - linha tracejada
