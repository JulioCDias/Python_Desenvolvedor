"""
Gerador de Expressao
"""

quadrados = (x**2 for x in range(10))
for i in quadrados:
    print(i)

print("#" * 20)


# exemplo 2 iterador infinito
def contador_infinito():
    i = 0
    while True:
        yield i
        i += 1


contador = contador_infinito()
for i in range(10):
    print(next(contador))

print("#" * 20)


# Coleta de Valores com send()
def coletar_valores():
    total = 0
    while True:
        valor = yield total
        if valor is None:
            break
        total += valor
        print(f"Recebi o valor {valor}")


coletor = coletar_valores()
next(coletor)  # Primeira chamada
print(coletor.send(10))
print(coletor.send(20))
print(coletor.send(30))

print("#" * 20)


# Tratamento de execeções
def gerador_de_excecoes():
    try:
        while True:
            valor = yield
            print(f"Valor recebido: {valor}")
    except ValueError:
        print("Valor inválido")


gerador = gerador_de_excecoes()
next(gerador)
gerador.send(10)
gerador.send(20)
# gerador.throw(ValueError)

print("#" * 20)


# Casacata de Geradores
def multiplicar_por_dois(iterable):
    for item in iterable:
        yield item * 2


def adicionar_cinco(iterable):
    for item in iterable:
        yield item + 5


numeros = range(5)
resultado = adicionar_cinco(multiplicar_por_dois(numeros))
for r in resultado:
    print(r)
