class VendasIterator:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.file = open(arquivo, "r", encoding="utf-8")

    def __iter__(self):
        return self

    def __next__(self):
        linha = self.file.readline()
        if not linha:
            self.file.close()
            raise StopIteration
        categoria, valor = linha.strip().split(",")
        return categoria, float(valor)


def gerador_soma_vendas(arquivo):
    total_vendas = 0
    for categoria, valor in VendasIterator(arquivo):
        total_vendas += valor
        yield categoria, valor, total_vendas


contagem_vendas = {}
arquivo = "vendas.txt"
print("Processando o arquivo de vendas...")
for categoria, valor, total in gerador_soma_vendas(arquivo):
    print(f"Categoria: {categoria}, Valor: {valor:.2f}, Total: {total:.2f}")

    # Contagem de vendas por categoria
    if categoria in contagem_vendas:
        contagem_vendas[categoria] += 1
    else:
        contagem_vendas[categoria] = 1

for categoria, contagem in contagem_vendas.items():
    print(f"Total de vendas para a categoria {categoria}: {contagem_vendas[categoria]}")
