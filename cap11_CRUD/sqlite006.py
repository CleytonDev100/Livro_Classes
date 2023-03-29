import sqlite3
from contextlib import closing

#Filtrando informações com o where, porém, agora usando uma mascara, para não sofrer sqlinject

nome = input("Qual nome deseja encontrar: ")
x = 0

with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select * from agenda where nome = ?", (nome,))
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if x == 0:
                    print("Nada encontrado...")
                break
            print(f"Nome - {resultado[0]}\nTelefone - {resultado[1]}")
            x += 1
