class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self._nome = nome
        self._preco = preco

    def mostrar_nome(self):
<<<<<<< HEAD
        return self._nome

    def alterar_preco(self, novo_preco):
        if novo_preco < 0:
            raise ValueError('Preço não pode ser negativo')
        self._preco = novo_preco

    def mostrar_preco(self):
        return self._preco
    
    def alterar_nome(self, novo_nome):
            if novo_nome.strip() == '':
                raise ValueError('nome não pode ser vazio')
            self._nome = novo_nome.strip()
            
    
=======
        pass

    def alterar_preco(self, novo_preco):
        if novo_preco < 0:
            return 'Proibido -  Valor inválido'
        
        self._preco = novo_preco

    def mostrar_preco(self):
        return self._preco
>>>>>>> origin/main
