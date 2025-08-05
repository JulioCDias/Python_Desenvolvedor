from abc import ABC, abstractmethod

class ItemBiblioteca(ABC):  # Classe abstrata
    def __init__(self, titulo, autor, preco):
        self._titulo = titulo
        self._autor = autor
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass