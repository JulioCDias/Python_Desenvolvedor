from modelos.biblioteca import Biblioteca
from modelos.items.livro import Livro
from modelos.items.revista import Revista

livro1 = Livro("Livro 1", "Autor 1", 10, "ISBN 1")
livro1.aplicar_desconto()
livro2 = Livro("Livro 2", "Autor 2", 20, "ISBN 2")
livro2.aplicar_desconto()
livro3 = Livro("Livro 3", "Autor 3", 30, "ISBN 3")
livro3.aplicar_desconto()

revista1 = Revista("Revista 1", "Editora 1", 15, 1)
revista1.aplicar_desconto()
revista2 = Revista("Revista 2", "Editora 2", 25, 2)
revista2.aplicar_desconto()
revista3 = Revista("Revista 3", "Editora 3", 35, 3)
revista3.aplicar_desconto()


biblioteca_cidade = Biblioteca("Biblioteca Cidade")  # Objeto
biblioteca_shopping = Biblioteca("Biblioteca Shopping")
biblioteca_cidade.alterna_estado()
biblioteca_shopping.alterna_estado()
biblioteca_cidade.adicionar_item(livro1)
biblioteca_cidade.adicionar_item(livro2)
biblioteca_cidade.adicionar_item(revista1)
biblioteca_shopping.adicionar_item(livro3)
biblioteca_shopping.adicionar_item(revista2)
biblioteca_shopping.adicionar_item(revista3)
biblioteca_cidade.receber_avaliacao("Joao", 5, "Muito bom")
biblioteca_shopping.receber_avaliacao("Maria", 4, "Bom")


def main():
    Biblioteca.listar_bibliotecas()
    biblioteca_cidade.existem_itens()
    biblioteca_shopping.existem_itens()
    
    

if __name__ == "__main__":
    main()