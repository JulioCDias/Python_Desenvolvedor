class Game:
    def __init__(self, name, yaerLaunch, multiplayer, note):
        self.name = name
        self.yaerLaunch = yaerLaunch
        self.multiplayer = multiplayer
        self.note = note
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


game1 = Game("Lol", 2006, False, 8.0)
game1.tecnical_sheet()
game1.evaluate(9.0)
game1.evaluate(8.0)
game1.average()
game2 = Game("Fortnite", 2017, True, 8.0)
game2.tecnical_sheet()
game2.evaluate(10.0)
game2.evaluate(7)
game2.average()
