movieDescription = """
Top Gun Maverick é um filme de acao de 2023.
O filme foi dirigido por Joseph Kosinski.
Muito bom!
"""

print(movieDescription.upper())  # Maiuscula
print(movieDescription.lower())  # Minuscula
print(movieDescription.title())  # Primeira letra maiuscula
print(movieDescription.capitalize())  # Primeira letra maiuscula
print(movieDescription.center(10, "*"))  # Centralizar
print(movieDescription.swapcase())  # Inverter maiuscula e minuscula

print(len(movieDescription))  # Quantidade de caracteres
print(movieDescription.find("J"))  # Busca dentro da string
