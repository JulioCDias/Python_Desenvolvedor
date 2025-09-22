from fastapi import FastAPI

app = FastAPI()

jogadores = {
    "1": "Jogador 1",
    "2": "Jogador 2",
    "3": "Jogador 3",
    "4": "Jogador 4",
}


@app.get("/")
async def root():
    return jogadores
