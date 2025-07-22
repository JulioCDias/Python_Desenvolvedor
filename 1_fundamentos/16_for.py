# Lista de Filmes

filmlist = [
    "Star Wars",
    "Vingadores",
    "Matrix",
    "Liga da Justiça"
]

for filme in filmlist:
    print(filme)

print("=" * 50)

for filme in enumerate(filmlist):  # Enumerar
    print(filme)

print("=" * 50)
for filme in filmlist:  # Break - Parar, nao da pra usar no enumerate
    if filme == "Vingadores":
        break
    print(filme)

print("=" * 50)
for filme in filmlist:  # Continue - Pular
    if filme == "Vingadores":
        continue
    print(filme)


# Avaliação de Filmes
movieName = input("Qual o nome do filme? \n")
movierating = int(input("Digite quantas avaliaçoes que deseja fazer \n"))
total = 0

for i in range(movierating):
    noteMovie = float(input("Digite a nota do filme? \n"))
    total += noteMovie

if movierating > 0:
    average = total / movierating
else:
    average = 0

print(f"{movieName} - {average:.2f} - {movierating}")
