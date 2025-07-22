# 1 - funçaõ para imprimir nome completo

def print_full_name(first_name, last_name):
    print(first_name + " " + last_name)


print_full_name("Maria", "Silva")

# 2 Função para somar 2 numeros


def sum(num1, num2):
    return num1 + num2


print(f"A soma é {sum(1, 2)}")

# 3 - Função com paramenmtro default


def adrres(coutry="Brasil"):
    print("Estou morando em " + coutry)


adrres()
adrres("Portugal")

# 4 função para avaliar filme


def rate_movie(num_ratings, movie_name):
    total = 0

    for i in range(num_ratings):
        rating = float(input(f"Digite a avaliacao {i + 1}: "))
        total += rating

    if num_ratings > 0:
        average = total / num_ratings
        print(f"A media das avaliacoes do filme {movie_name} é: {average:.2f}")
        return average
    else:
        print("Nenhuma avaliacao foi fornecida.")
        return None


rate_movie(3, "Vingadores")
