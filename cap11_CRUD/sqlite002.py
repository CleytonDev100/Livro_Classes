import sqlite3

#Inserindo algumas informações no banco de dados, insert into

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute("create table OK (OK2 text, OK3 text)")
cursor.execute("insert into OK (OK2, OK3) values(?,?)", ("Cleyton", "12"))
conexao.commit()
cursor.close()
conexao.close()

# Pegando informações de um banco de dados

conexao = sqlite3.connect("agenda.db") #Sempre fazendo a conexão primeiro
cursor = conexao.cursor() # Criando o cursor
cursor.execute("select * from agenda") #(select tudo) from agenda
resultado = cursor.fetchone() #Vem em forma de tupla (fetchone) = transforma as informações em TUPLA
print(f"O nome é {resultado[0]} o Telefone é {resultado[1]}")
cursor.close()
conexao.close()
