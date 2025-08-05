import sqlite3

conn = sqlite3.connect('database.db')
print("Conectado ao banco de dados")

conn.close()
print("Desconectado do banco de dados")