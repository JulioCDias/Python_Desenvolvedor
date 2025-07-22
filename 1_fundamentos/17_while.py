filmlist = [
    "Star Wars",
    "Vingadores",
    "Matrix",
    "Liga da Justiça"
]

index = 0
while index < len(filmlist):
    print(filmlist[index])
    index += 1

# 2 - QUANDO CONDIÇÃO FOR ATENDIDA O LOOP ENTERROMPE
index = 0
while index < len(filmlist):
    print(filmlist[index])
    if filmlist[index] == "Liga da Justiça":
        break
    index += 1

# 3 - QUANDO CONDIÇÃO FOR ATENDIDA O LOOP PULA O ITEM
index = 0
while index < len(filmlist):
    print(filmlist[index])
    if filmlist[index] == "Liga da Justiça":
        index += 1
        continue
    index += 1

# 4 Avaliação com while
movieName = input("Qual o nome do filme? \n")
movierating = int(input("Digite quantas avaliaçoes que deseja fazer \n"))

total = 0
count = 0

while count < movierating:
    rating = int(input("Digite a nota do filme \n"))
    total += rating
    count += 1

average = total / movierating

print(f"O filme {movieName} tem {average:.2f} de nota")
