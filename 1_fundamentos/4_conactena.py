name = input("Qual o nome do filme? \n")
yaerLaunch = int(input("Qual o ano de lançamento? \n"))  # casting
noteMovie = float(input("Qual a nota do filme? \n"))

print(name + " - " + str(yaerLaunch) + " - " + str(noteMovie))  # Concatenação

print(f"{name} - {yaerLaunch} - {noteMovie}")  # Interpolação

print("{0} - {1} - {2}".format(name, yaerLaunch, noteMovie))  # Formatação
