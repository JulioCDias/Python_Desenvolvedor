class NomeComLetra:
    def __init__(self, nome, letra):
        self.nome = nome
        self.letra = letra
        self.indice = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.indice < len(self.nome):
            nome = self.nome[self.indice]
            self.indice += 1
            if nome.startswith(self.letra):
                return nome
        raise StopIteration
    
# Exemplo de uso do iterador
lista_nomes = ["Ana", "Bruno", "Alice", "Carlos", "Amanda", "Beatriz", "Cristina", "Davi", "Eduardo", "Fernanda"]
letra = "A"
iterador_nomes = NomeComLetra(lista_nomes, letra)

for nome in iterador_nomes:
    print(nome)