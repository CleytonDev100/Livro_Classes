import sqlite3
from contextlib import closing


porcentagem = int(input("Em quantos % o preço irá subir: ")) # Determina o quanto um preço irá subir

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select preco from produtos") # Pega TODOS os preços da tabela produtos
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            else:
                cursor.execute(f"update produtos set preco = {resultado[0] + porcentagem / 100 + resultado[0]}") # Aumenta os preços dos produtos
                conexao.commit() # Guarda esses novos dados
                if cursor.rowcount == 1:
                    print(f"Mudei {cursor.rowcount} dado")
                else:
                    print(f"Mudei {cursor.rowcount} dados")
