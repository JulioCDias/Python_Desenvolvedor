import statistics

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

media = statistics.mean(numeros)
mediana = statistics.median(numeros)
moda = statistics.mode(numeros)
variancia = statistics.variance(numeros)
desvio_padrao = statistics.stdev(numeros)

print(f"Media: {media}") # Media
print(f"Mediana: {mediana}") # Mediana
print(f"Moda: {moda}") # Moda
print(f"Variancia: {variancia}") # Variancia
print(f"Desvio Padrao: {desvio_padrao}") # Desvio Padrao, desvio padrao eh a raiz quadrada da variancia
