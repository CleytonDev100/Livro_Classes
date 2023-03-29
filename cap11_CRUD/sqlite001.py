# Aprendendo a criar uma tabela no banco de dados (create table) = C

import sqlite3

conexao = sqlite3.connect("agenda.db") #connect = conecta a variavel a o arquivo
curso = conexao.cursor() #cursor = cria uma ponte para retirar, colocar e deletar dados
curso.execute("create table agenda(nome text, telefone text)") #execute = executa, ele cria ou apaga ou pega dados,
# #create table
curso.execute("insert into agenda (nome, telefone) values(?,?)", ("Cleyton", "199132"))
conexao.commit() #commit = commita, muda a tabela
curso.close() # para a variavel
conexao.close()
