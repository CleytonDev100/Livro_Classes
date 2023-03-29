from contextlib import closing
import sqlite3

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        nome = input("Nome: ").lower()
        preco = int(input("Preço: "))
        cursor.execute("insert into produtos (nome, preco) values(?,?)", (nome, preco))
        conexao.commit()
