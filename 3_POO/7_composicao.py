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


class GameStudio:
    def __init__(self, name=""):
        self.name = name
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def evaluate_studio_quality(self):
        total_notes = sum(game.note for game in self.games)
        num_games = len(self.games)
        if num_games == 0:
            print(f"O estudio {self.name} ainda nao lançou nenhum jogo")
        else:
            average_note = total_notes / num_games
            print(
                f"Avaliacao medio dos Jogos o estudio {self.name}: {average_note:.2f}")


game1 = Game("Lol", 2006, False, 8.0)
game2 = Game("Fortnite", 2017, True, 7.0)

studio = GameStudio("Awesome Games")
studio.add_game(game1)
studio.add_game(game2)

studio.evaluate_studio_quality()

for game in studio.games:
    game.tecnical_sheet()
