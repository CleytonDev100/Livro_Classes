import sqlite3
from contextlib import closing

# Aprendemos sobre o rowcount, que mostra quantos vezes o cursor foi rodado (acho)

with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("update agenda set telefone = '123-456'")
        print(f"Registros mudados - {cursor.rowcount}")
