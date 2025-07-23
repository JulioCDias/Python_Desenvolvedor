from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 Lita de Frutas (contagem)
fruits = [
    'banana',
    'banana',
    'maca',
    'banana',
    'laranja',
    'laranja',
    'banana'
]

counter = Counter(fruits)
print(counter)
print(counter['banana'])

# 2 - Utilizando tupla nomeada
game = namedtuple('game', ['name', 'platform', 'year'])
g1 = game('Super Mario Bros', 'SNES', 1998)
g2 = game('Mega Man', 'SNES', 1998)

print(g1)
print(g2)
print("**"*50)

# 3 - Ordenando Dicionarios
staudents = {
    "joao": 23,
    "maria": 21,
    "pedro": 25,
    "julio": 29
}
a = sorted(staudents.items(), key=itemgetter(0))  # Ordena por [0] chave
b = sorted(staudents.items(), key=itemgetter(1))  # Ordena por [1] valor
print(a)
print(b)
print("**"*50)

# 4 - Fila
q = deque(maxlen=3)
q.append('a')
q.append('b')
q.append('c')
q.append('d')

print(q)