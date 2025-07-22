"""
* args - argumentos não nomeados, quando nao sabemos quantos argumentos serao passados.
        os argumentos sao pasados como uma tupla
* kwargs - argumentos nomeados, alem dos valores podemos passar as recpetivas chaves para cada argumento
        os argumentos sao passados como um dicionario
"""

# *args


def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(sum_total)


sum(7)
sum(7, 8)
sum(7, 8, 9)

# **kwargs


def presentation(**data):
    for key, value in data.items():
        print(f"{key}: {value}")


presentation(name="Julio", age=30)
presentation(name="Julio", age=30, job="Programmer")
