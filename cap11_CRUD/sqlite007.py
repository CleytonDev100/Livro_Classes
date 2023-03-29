import sqlite3
from contextlib import closing

# Aprendemos a mudar um dado, com o update = U

with sqlite3.connect("agenda.db") as conexao:
     with closing(conexao.cursor()) as cursor:
         cursor.execute("update agenda set telefone = '19998319351'")
     conexao.commit()

with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select * from agenda")
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f"Nome - {resultado[0]}\nTelefone - {resultado[1]}")

