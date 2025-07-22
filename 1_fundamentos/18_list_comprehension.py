# Litar valores de 0 a 10 que seja menores que 4
# usando for
numbers = []

for i in range(11):
    if i < 4:
        numbers.append(i)

print(numbers)

# usando list comprehension
numbers = [i for i in range(11) if i < 4]
print(numbers)

# 2 - filmes que possuem a letra "i" no titulo
filmlist = [
    "Star Wars",
    "Vingadores",
    "Matrix",
    "Liga da Justiça"
]

filmesComI = [filme for filme in filmlist if "i" in filme]
print(filmesComI)

# 3 - Filmes que eu assisti
filmesAssistidos = [filme for filme in filmlist if filme != "Vingadores"]
print(filmesAssistidos)

# 4 ENcontrando o filme pelo nome

while True:
    filme = input("Qual filme deseja encontrar? (ou 'sair' para Encerrar)\n")
    if filme.lower() == "sair":
        break

    filmeEncontrado = [f for f in filmlist if filme.lower() in f.lower()]

    if filmeEncontrado:
        print(
            f"Sim, o(s) filme(s) contendo '{filme}' está(ão) na nossa lista:")
        for f in filmeEncontrado:
            print(f"- {f}")
    else:
        print(f"O filme '{filme}' não está na nossa lista.")
        
