import sqlite3
from contextlib import closing

# Deletar dados, com o delete from

with sqlite3.connect("agenda2.0.db") as conexao:
    for registro in conexao.execute("select * from agenda"):
        print(registro)

    with closing(conexao.cursor()) as cursor:
        cursor.execute("delete from agenda where nome = 'João'")
        print(f"Registros apagados: {cursor.rowcount}")
        if cursor.rowcount == 1:
            conexao.commit()
            print(f"Operação salva!")
        else:
            conexao.rollback()
            print(f"Operação anulada!")
