"""
Yield - Gerador
- É ima plavra  chave para crioar geradores. Quando voçe usa ele um uma função, voçe tranforma a função em
    um gerador, que é um tipo especial de iterador.
- Ao invocar a função, ela no retorna um valor, mas sim um objeto gerador.
- deferenças entre return e yield:
    - return: finaliza a funcao e retorna um valor
    - yield: pausa a funcao e retorna um valor, mas mantem o estado da funcao para a proxima chamada
"""
def numeros_impares(n):
    for i in range(1, n+1, 2):
        yield i

for numero in numeros_impares(10):
    print(numero)


def linhas_com_numeros_de_palavras(arquivo, numero):
    with open(arquivo, 'r', encoding='utf-8') as file:
        for linha in file:
            if len(linha.split()) == numero:
                yield linha.strip()

arquivo = 'texto.txt'
for linha in linhas_com_numeros_de_palavras(arquivo, 3):
    print(linha)