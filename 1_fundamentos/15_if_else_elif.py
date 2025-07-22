# Informaçoes dobre o filme
name = input("Qual o nome do filme? \n")
yaerLaunch = int(input("Qual o ano de lançamento? \n"))  # casting
noteMovie = float(input("Qual a nota do filme? \n"))

if noteMovie > 7 and yaerLaunch > 2015:
    print(f"{name} - {yaerLaunch} - {noteMovie} - LINDO")
else:
    print(f"{name} - {yaerLaunch} - {noteMovie} - RUIM")

print("$"*100)
# Calculadora

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operation = input("Digite a operação desejada (+, -, *, /): ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Não é possível dividir por zero")
else:
    print("Operação inválida")
