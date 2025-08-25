import itertools

print("#"*20)
print("Iteradores Range")
#Exemplo 1 Range()
for i in range(5):
    print(i)

#Exemplo 2 Iterar Lista
print("#"*20)
print("Iteradores Lista")
lista = ['Ana', 'Bruno', 'Carlos']
for nome in lista:
    print(nome)

# Exemplo iterador Dicionario
print("#"*20)
print("Iteradores Dicionario")
dicionario = {'nome': 'Ana', 'idade': 25, 'cidade': 'São Paulo'}
for chave in dicionario:
    print(chave, dicionario[chave])

#exemplo enumerate
print("#"*20)
print("Iteradores Enumerate")
lista = ['Ana', 'Bruno', 'Carlos']
for index, nome in enumerate(lista):
    print(index, nome)

# Exemplo zip
print("#"*20)
print("Iteradores Zip")
nomes = ['Ana', 'Bruno', 'Carlos']
idades = [25, 30, 35]
for nome, idade in zip(nomes, idades):
    print(nome, idade)

# Exemplo itertools
print("#"*20)
print("Iteradores Itertools")
for i in itertools.count(start=10, step=2):
    if i > 20:
        break
    print(i)