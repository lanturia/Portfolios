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
    
def delete(x):
    c.execute("delete from login where id="+ x)
    dbase.commit()

def atualizar():
    c = dbase.cursor()
    c.execute(''' SELECT * from login''')
    data = c.fetchall()
    dbase.commit()
    return data

def alterar(x,y,z):
    atualizar()
    c.execute('SELECT * from login where id='+ x)
    rusuario=y[0][1]
    rsenha=z[0][2]
    if(len(y)==0):
        y = rusuario
    if(len(z)==0):
        z = rsenha
    c.execute("update login set usuario="+y+", senha"+z+"where"+x)
    dbase.commit()
