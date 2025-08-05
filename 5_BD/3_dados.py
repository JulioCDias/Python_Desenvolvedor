import sqlite3

conn = sqlite3.connect('database.db')
print("Conectado ao banco de dados")

cursor = conn.cursor()

cursor.execute(
    """
        INSERT INTO filmes (nome, ano, nota)
        VALUES ('Sonic', 2020, 7.5);
    """
    )

conn.commit()
print("Dados inseridos com sucesso")

conn.close()
print("Desconectado do banco de dados")