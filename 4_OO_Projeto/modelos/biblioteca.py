from modelos.avaliacao import Avaliacao
from modelos.items.item_biblioteca import ItemBiblioteca
class Biblioteca:  # Classe
    bibliotecas = []  # Atributo

    def __init__(self, nome):  # metodo construtor
        self.nome = nome
        self._ativo = False  # atributo privado
        self._avaliacoes = []
        self._itens = []
        Biblioteca.bibliotecas.append(self)  # type: ignore

    def __str__(self):  # Metodo especial
        return self.nome

    @classmethod  # Decorador que
    def listar_bibliotecas(cls):
        print("\n ### LISTA DE BIBLIOTECAS | NOTA MEDIA | STATUS ###")
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome.ljust(25)} | {biblioteca.media_avaliacoes} | {biblioteca.ativo}")

    def alterna_estado(self):  # Metodo modificador de estado Metodo SET
        self._ativo = not self._ativo

    @property  # Decorador de propriedade, representa o metodo GET
    def ativo(self):
        return "atiavada" if self._ativo else "desativada"

    def receber_avaliacao(self, cliente, nota, comentario):
        avaliacao = Avaliacao(cliente, nota, comentario)
        self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return '-'
        
        soma = sum(avaliacao.nota for avaliacao in self._avaliacoes)
        media = round(soma / len(self._avaliacoes),1)
        return media

    def adicionar_item(self, item):
        if isinstance(item, ItemBiblioteca):
            self._itens.append(item)

    def existem_itens(self):
        print(f"\n Itens na biblioteca: {self.nome}\n") 
        for i , item in enumerate(self._itens, 1):
            if hasattr(item, "isbn"):
                msg_livro = f"{i} - Livro: {item._titulo} | Autor: {item._autor} | Preco: {item._preco} | ISBN: {item.isbn}"
                print(msg_livro)
            else:
                msg_revista = f"{i} - Revista: {item._titulo} | Autor: {item._autor} | Preco: {item._preco} | Edicao: {item.edicao}"
                print(msg_revista)

