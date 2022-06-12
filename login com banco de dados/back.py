import sqlite3

dbase = sqlite3.connect('login.db')
c = dbase.cursor()
dbase.execute(''' CREATE TABLE IF NOT EXISTS login(
                  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                  usuario TEXT NOT NULL,
                  senha TEXT NOT NULL)''')
dbase.commit()

def cadastro(usuario,senha):
    c.execute(''' INSERT INTO login(id, usuario, senha) VALUES(NULL, ?, ?)''', (usuario, senha))
    dbase.commit()
