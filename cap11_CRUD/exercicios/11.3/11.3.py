import sqlite3
from contextlib import closing

nome = input("Quer saber o preço de qual produto: ")
with sqlite3.connect("../11.1/precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select preco from produtos where nome = ?", (nome, ))
        x = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if x == 0:
                    print("Não encontramos nada...")
                break
            x += 1
            print(f"Produto {nome} - {resultado[0]}R$")

