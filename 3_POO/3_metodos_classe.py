class Game:
    """
    Nao posso ter muyltiplos contrutores em python porem posso
    1. Usar argumentos opcionais no __init__
    Você pode definir um único método __init__ com argumentos padrão (opcionais)
    ou argumentos variáveis (*args, **kwargs) para permitir diferentes formas de inicialização.
    2.Usar métodos de classe (@classmethod)
    Você pode criar métodos de classe para oferecer diferentes formas de criar instâncias da classe,
    funcionando como "construtores alternativos".
    3. Usar argumentos variáveis (*args, **kwargs)
    Você pode usar *args e **kwargs para criar um __init__ que aceita diferentes números e
    tipos de argumentos, tratando-os conforme necessário.
    4. Herança e __init__ em classes filhas
    Se você tem uma classe filha, ela pode ter seu próprio __init__, mas isso não significa
    "múltiplos __init__" na mesma classe. A classe filha pode chamar o __init__ da classe pai
    usando super() ou definir sua própria lógica de inicialização.
    """

    def __init__(self, name, yaerLaunch, multiplayer, note):
        self.name = name
        self.yaerLaunch = yaerLaunch
        self.multiplayer = multiplayer
        self.note = note

    def __str__(self):
        return f"Name: {self.name} - Year Launch: {self.yaerLaunch} - Multiplayer: {self.multiplayer} - Note: {self.note}"


game1 = Game("Lol", 2006, False, 8.0)
game2 = Game("Fortnite", 2017, True, 8.0)

print(game1)
print(game2)
