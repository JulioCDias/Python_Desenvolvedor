import sqlite3

conn = sqlite3.connect('database.db')
print("Conectado ao banco de dados")

cursor = conn.cursor()

id = 2

cursor.execute(
    """
        DELETE FROM filmes
        WHERE id = ?
    """,
    (id,)
    )

conn.commit()
print("Dados excluidos com sucesso")

conn.close()
print("Desconectado do banco de dados")