from contextlib import closing
import sqlite3

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select preco from produtos")
        x = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f"O preço {x} é - {resultado[0]}")
            x += 1
