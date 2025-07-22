filmesSet = {
    "Star Wars",
    "Vingadores",
    "Matrix",
    "Liga da Justiça"
}

print(filmesSet)
print(type(filmesSet))

# Buscar o tamnhao do set
print(len(filmesSet))

# 2 - True e 1 sao considerados o mesmo valor
exemploSet = {
    "Matrix", True, 1, 8.7
}

print(exemploSet)

# 3 - Adicionar um item
filmesSet.add("Avatar")
print(filmesSet)

# 4 - Remover um item
filmesSet.remove("Liga da Justiça")
print(filmesSet)

# 5 - Verificar se um item existe
print("Matrix" in filmesSet)

# 6 - Copiar um set
filmesSet2 = filmesSet.copy()
print(filmesSet2)
