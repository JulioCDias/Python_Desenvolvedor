import sqlite3

def conectar_bd():
    conn = sqlite3.connect('database.db')
    print("Conectado ao banco de dados")
    return conn

def inserir_dados(nome, ano, nota):
    conn = conectar_bd()
    cursor = conn.cursor()

    cursor.execute(
        """
            INSERT INTO filmes (nome, ano, nota)
            VALUES (?, ?, ?);
        """,(nome, ano, nota)
        )

    conn.commit()
    conn.close()
    print("Dados inseridos com sucesso")

def obter_dados():
    conn = conectar_bd()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM filmes")

    dados = cursor.fetchall()
    conn.close()
    return dados