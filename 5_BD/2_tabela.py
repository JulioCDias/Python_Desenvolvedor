import sqlite3

conn = sqlite3.connect('database.db')
print("Conectado ao banco de dados")

cursor = conn.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL
        );
    """
    )

conn.close()
print("Desconectado do banco de dados")