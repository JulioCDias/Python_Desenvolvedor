filmsTuple = (
    "Star Wars",
    "Vingadores",
    "Matrix",
    "Liga da Justiça"
)

print(filmsTuple)
print(type(filmsTuple))

# 1 Buscar os dois primeirios filmes
print(filmsTuple[0:2])
# 2 Buscar o ultimo filmes
print(filmsTuple[-1:])
# 3 Buscar o filme de uma posicao especifica
print(filmsTuple[2])

# 4 Buscar o filme de uma posicao especifica
print(filmsTuple.index("Matrix"))

# buscar filme de uma posição em diante
print(filmsTuple[2:])
