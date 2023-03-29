import sqlite3
from contextlib import closing

#Pegando informações filtradas do banco de dados (where) = R

with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select * from agenda where nome = 'Antonio'")
        while True:
            resultado = cursor.fetchone()
            if resultado == None:
                break
            print(f"Nome = {resultado[0]}. Telefone = {resultado[1]}")

