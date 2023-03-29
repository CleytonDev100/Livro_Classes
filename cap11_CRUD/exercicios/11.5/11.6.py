import sqlite3
from contextlib import closing

x = 0

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        nome = input("Nome do produto: ")
        np = int(input("Novo preço do produto: "))
        cursor.execute("select preco from produtos where nome = ?", (nome, )) # seleciona todos os precos dos produtos que tenham o nome como o valor da variavel
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if x == 0:
                    print("Não encontramos esse produto...")
                break
            else:
                cursor.execute(f"update produtos set preco = {np} where nome = ?", (nome, )) # where é necessario pois, senhão irá mudar TODOS os campos preco
                print(f"Tivemos {cursor.rowcount} mudanças")
                conexao.commit()
            x += 1
