import re


text = "Ola, tudo bem? Estou aprendendo Python"
# 1 - Indice Inicial e Final de Palavras
# O r significa raw string (string crua)
match = re.search(r"Python", text)
print(f"Indice Inicial: {match.start()}")  # type: ignore
print(f"Indice Final: {match.end()}")  # type: ignore
print(re.search("Python", text))

# 2 Buscando o indice que possui o Ponto
site = "http://www.google.com.br"
match = re.search(r"\.", site)
print(match.start())  # type: ignore

# 3 Buscando uma lista de caracteres dentro de uma frase
text = "Ola, tudo bem? Estou aprendendo Python"
pattern = "[a-m]"
result = re.findall(pattern, text)
print(result)

# 4 verificando o inicio de uma string
rule = r"^A"
phrases = [
    'A casa esta suja',
    'O dia esta lindo',
    'Vamos aprender Python',
    'Hora de passear'
]

for phrase in phrases:
    match = re.search(rule, phrase)
    if match:
        print(f"Corresponde: {phrase}")
    else:
        print(f"Nao corresponde: {phrase}")

# 5 verificando o fim de uma string
rule = r"Python$"
phrases = [
    'A casa esta suja',
    'O dia esta lindo',
    'Vamos aprender Python',
    'Hora de passear'
]

for phrase in phrases:
    match = re.search(rule, phrase)
    if match:
        print(f"Corresponde: {phrase}")
    else:
        print(f"Nao corresponde: {phrase}")