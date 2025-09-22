import re


def explorar_expressao_regular(texto):
    padrao = r"\bPython\b"
    if re.search(padrao, texto):
        print("O padrao foi encontrado")
    else:
        print("O padrao nao foi encontrado")


texto = "Ola, tudo bem? Estou aprendendo Python"
explorar_expressao_regular(texto)
