import sqlite3

conn = sqlite3.connect('database.db')
print("Conectado ao banco de dados")

cursor = conn.cursor()

dados = cursor.execute("SELECT * FROM filmes")

print(dados.fetchall())
print("Desconectado do banco de dados")
conn.close()