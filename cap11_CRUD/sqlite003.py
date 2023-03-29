#inserindo varias informações de um banco de dados, usando executemany

import sqlite3
dados = [("Pedro", "19-02132-1"), ("João", "01293210983"), ("Antonio", "012983210839")]


conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.executemany("insert into agenda (nome, telefone) values(?,?)", dados)
conexao.commit()
cursor.close()
conexao.close()

