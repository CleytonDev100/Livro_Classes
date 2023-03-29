import sqlite3
from contextlib import closing

#Dando a oportunidade do cliente poder buscar suas informações, usando uma variavel e o where

nome = input("Qual usuario pretende procurar: ")

with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute(f"select * from agenda where nome = '{nome}'")
        resultado = cursor.fetchone()

print(f"Nome - {resultado[0]}\nTelefone - {resultado[1]}")
