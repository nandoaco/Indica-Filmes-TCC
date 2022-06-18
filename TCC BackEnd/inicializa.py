import sqlite3
import os.path
import os

nome_banco = "filmes.db"

if os.path.exists(nome_banco):
    os.unlink(nome_banco)

conexao = sqlite3.connect(nome_banco)
cursor = conexao.cursor()

consulta = """CREATE TABLE Filmes (
    id INTEGER AUTO_INCREMENT, 
    titulo TEXT,
    imagem TEXT,
    sinopse TEXT
    )"""

cursor.execute(consulta)
conexao.close()

