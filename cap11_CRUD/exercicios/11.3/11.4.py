import sqlite3
from contextlib import closing

v1 = input("Valor1: ")
v2 = input("Valor2: ")

with sqlite3.connect("../11.1/precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select * from produtos")
        resultado = cursor.fetchall()
        for valor in resultado:
            if valor[0] == v1:
                pass
            elif valor[0] == v2:
                pass
            else:
                print("-="*20)
                print(f"Nome: {valor[0]}\nPreço: \033[31;1m{valor[1]}\033[m")
                print("-=" * 20)
