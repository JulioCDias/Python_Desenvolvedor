import random

# 1 - Gerar um numero aleatorio
print(random.randint(1, 100))

# 2 - Sortear um item de uma lista
lista = ["Fulano", "Ciclano", "Beltrano"]
print(random.choice(lista))

# 3 Gerar um caractere aleatorio
print(random.choice("Curso Python"))

# 4 gerar mais de umn valor aleatorio
print(random.sample(range(100), 5))

# 5 - Programa de sorteio
done = False
while not done:
    print("1 - Sortear um numero aleatorio")
    print("2 - Sortear um item de uma lista")
    print("3 - Gerar um caractere aleatorio")
    print("4 - Gerar mais de um valor aleatorio")
    print("5 - Sair")
    option = input("Digite a opcao desejada: ")
    if option == "1":
        print(random.randint(1, 100))
    elif option == "2":
        lista = ["Fulano", "Ciclano", "Beltrano"]
        print(random.choice(lista))
    elif option == "3":
        print(random.choice("Curso Python"))
    elif option == "4":
        print(random.sample(range(100), 5))
    elif option == "5":
        done = True