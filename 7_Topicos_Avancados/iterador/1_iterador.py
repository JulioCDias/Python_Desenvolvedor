class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.atual = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual > self.limite:
            raise StopIteration
        else:
            valor_atual = self.atual
            self.atual += 1
            return valor_atual
        
# Exemplo de uso do iterador
contador = Contador(5)

for numero in contador:
    print(numero)
    
# Saída esperada:
# 1
# 2
# 3
# 4
# 5
# O iterador Contador permite iterar de 1 até o limite especificado.