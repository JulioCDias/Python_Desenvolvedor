import sqlite3

conn = sqlite3.connect('database.db')
print("Conectado ao banco de dados")

cursor = conn.cursor()

id = 2

cursor.execute(
    """
        UPDATE filmes
        SET nome = 'Star Wars 2'
        WHERE id = ?
    """,
    (id,)
    )

conn.commit()
print("Dados atualizados com sucesso")

conn.close()
print("Desconectado do banco de dados")