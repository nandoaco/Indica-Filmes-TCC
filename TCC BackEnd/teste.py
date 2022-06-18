import sqlite3

nome_banco = "filmes.db"
con = sqlite3.connect(nome_banco)
cur = con.cursor()

cur.execute("SELECT * FROM Filmes")
dados = cur.fetchall()
print(dados)
con.close()