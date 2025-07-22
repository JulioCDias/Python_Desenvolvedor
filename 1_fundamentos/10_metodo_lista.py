filmlist = [
    "Star Wars",
    "Vingadores",
    "Matrix",
    "Liga da Justiça"
]

# 1 tamanho da lista
print(len(filmlist))

# recuperar item pelo nome
print(filmlist.index("Liga da Justiça"))

# recuperar item pelo index
print(filmlist[2])

# add item na lista
filmlist.append("Avatar")
print(filmlist)

# remover item da lista
filmlist.remove("Liga da Justiça")
print(filmlist)

# Ordenar a lista
filmlist.sort()
print(filmlist)

# copiar uma lista
filmlist2 = filmlist.copy()
print(filmlist2)

# limpar a lista
filmlist.clear()
print(filmlist)