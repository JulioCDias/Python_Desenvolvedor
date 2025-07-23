# Classe Pai (Super Classe) - Generalista
class Game:
    total_games = 0  # variafvel de classe

    def __init__(self, name, yaerLaunch, multiplayer, note):
        self.name = name
        self.yaerLaunch = yaerLaunch
        self.multiplayer = multiplayer
        self.note = note
        Game.total_games += 1
        self.totalEvaluation = 0
        self.evaluators = 0

    def __str__(self):
        return f"Name: {self.name} - Year Launch: {self.yaerLaunch} - Multiplayer: {self.multiplayer} - Note: {self.note}"

    def tecnical_sheet(self):
        print("\n### DADOS DO JOGO ###")
        print(f" Nome do Jogo: {self.name}.")
        print(f" Ano de lançamento: {self.yaerLaunch}")
        print(f" Modo Multiplayer?: {self.multiplayer}")
        print(f" Avaliaçaõ do Jogo: {self.note}")

    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        print(
            f"Nota Media do Jogo {self.name}: {self.totalEvaluation / self.evaluators}")


# Classe Derivada (Subclasse) - Classe filha - esapecializada
class SinglePlayerGame(Game):  # Herança
    def __init__(self, name="", yaerLaunch=0, note=0.0, storyline=""):
        super().__init__(name, yaerLaunch, multiplayer=False, note=note)
        self.storyline = storyline

    def tecnical_sheet(self):
        super().tecnical_sheet()
        print(f"Enredo: {self.storyline}")


mult_game = Game("Fortinite", 2017, True, 8.0)
mult_game.tecnical_sheet()

single_game = SinglePlayerGame(
    "The last os Us", 2020, 9.5, "Emocionante Historia")
single_game.tecnical_sheet()
