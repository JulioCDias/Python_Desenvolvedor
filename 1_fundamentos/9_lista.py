filmeMatrix = []  # Lista vazia
print(type(filmeMatrix))  # <class 'list'>

filmeMatrix = ["Matrix", 1999, 8.7, True]
print(filmeMatrix)

filmsList = [  # Lista de listas
    ["Matrix", 1999, 8.7, True],
    ["Matrix 2", 2003, 8.7, True],
    ["Matrix 3", 2003, 8.7, True],
]

print(filmsList)  # Listas aninhadas
print(filmsList[0])  # Listas aninhadas
print(filmsList[0][0])  # Listas aninhadas

filmlist = [
    "Star Wars",
    "Vingadores",
    "Matrix",
    "Liga da Justiça"
]

print(filmlist)

# 1 Buscar os dois primeirios filmes
print(filmlist[0:2])
# 2 Buscar os dois ultimos filmes
print(filmlist[-2:])
# 3 Buscar o filme de 2023
print(filmlist[filmlist.index("Matrix")])