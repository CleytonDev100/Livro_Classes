import sqlite3
from contextlib import closing

#Mudar as informações usando o update, porém com o where, para não mudar TODAS as informações

with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("update agenda set telefone = '1998319351' where nome = ?", ("Cleyton", ))
        if cursor.rowcount == 1:
            conexao.commit()
            print("Mudanças alteradas")
        else:
            conexao.rollback()
            print("Mudanças não alteradas")
