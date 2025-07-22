# Funçao
def welcome():
    print("Bem vindo ao Python")
    print("Estou aprendendo funcoes")


welcome()

# 2 - Função para calcular a media de notas


def calculate_average():
    num_ratings = int(input("Digite a quantidade de avaliacoes: "))
    total = 0

    for i in range(num_ratings):
        rating = float(input(f"Digite a avaliacao {i + 1}: "))
        total += rating

    if num_ratings > 0:
        average = total / num_ratings
        print(f"A media das avaliacoes é: {average:.2f}")
        return average
    else:
        print("Nenhuma avaliacao foi fornecida.")
        return None


calculate_average()


# 3 Cadastro de filmes
def create_movie():
    name = input("Qual o nome do filme? \n")
    yaerLaunch = int(input("Qual o ano de lançamento? \n"))  # casting
    noteMovie = float(input("Qual a nota do filme? \n"))
    print(f"{name} - {yaerLaunch} - {noteMovie}")


create_movie()
