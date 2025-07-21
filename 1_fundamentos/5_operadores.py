num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# ARITIMETICAS
print("A soma é: " + str(num1 + num2))
print("A subtração é: " + str(num1 - num2))
print("A multiplicação é: " + str(num1 * num2))
print("A divisão é: " + str(num1 / num2))
print("O resto da divisão é: " + str(num1 % num2))
print("A divisão inteira é: " + str(num1 // num2))

# Logicos
print("O primeiro número é maior que o segundo? " + str(num1 > num2))
print("O primeiro número é maior ou igual ao segundo? " + str(num1 >= num2))
print("O primeiro número é menor que o segundo? " + str(num1 < num2))
print("O primeiro número é menor ou igual ao segundo? " + str(num1 <= num2))
print("O primeiro número é igual ao segundo? " + str(num1 == num2))
print("O primeiro número é diferente ao segundo? " + str(num1 != num2))

# Atribuição
num1 += 1
print(num1)
num1 -= 1
print(num1)
num1 *= 2
print(num1)
num1 /= 2
print(num1)
num1 %= 2
print(num1)
