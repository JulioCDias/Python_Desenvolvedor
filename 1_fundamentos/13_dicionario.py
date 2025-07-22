filmInception = {  # Dicionario
    "name": "Inception",
    "yearLaunch": 2010,
    "note": 8.8,
    "planIncluded": True,
    "genres": ["Aventura", "Suspense", "Drama"]  # Lista
}

print(filmInception["name"])
print(filmInception["yearLaunch"])
print(filmInception["note"])
print(filmInception["planIncluded"])
print(filmInception["genres"])  # Busca no dicionario
print(filmInception.get("genres"))  # Busca no dicionario usando get

print(type(filmInception))
print(len(filmInception))

print(filmInception.keys())  # Busca as chaves
print(filmInception.values())  # Busca os valores

# Buscando ittem com chave e valor
print(filmInception.items())

# Adicionar um item
filmInception["Director"] = "Christopher Nolan"
print(filmInception)

# atualizar um item
filmInception["note"] = 9.0
print(filmInception)

# Utilizar update quando for atualizar mais de um item
filmInception.update({"note": 9.9})
print(filmInception)

# Remover um item
filmInception.pop("planIncluded")
print(filmInception)
