class Game:
    name = ""
    yaerLaunch = 0
    multiplayer = False
    note = 0.0


# Primeiro jogo
game1 = Game()
game1.name = "Minecraft"
game1.yaerLaunch = 2011
game1.multiplayer = True
game1.note = 9.0

# Segundo jogo
game2 = Game()
game2.name = "LOL"
game2.yaerLaunch = 2011
game2.multiplayer = True
game2.note = 9.0

print("Informacoes dos jogos:")
print(game1.name)
print(game1.yaerLaunch)
print(game1.multiplayer)
print(game1.note)
print("__"*50)
print(game2.name)
print(game2.yaerLaunch)
print(game2.multiplayer)
print(game2.note)
