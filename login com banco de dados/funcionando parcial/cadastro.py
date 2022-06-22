import sqlite3
import PySimpleGUI as sg
import back

def visualiza_bd():
    back.dbase = sqlite3.connect('login.db')
    c = back.dbase.cursor()
    c.execute(''' SELECT * from login''')
    data = c.fetchall()
    back.dbase.commit()
    return data

sg.theme('Dark Amber') # Tema das janelas   

id = visualiza_bd()
login = visualiza_bd()

layout = [
            [sg.Text('Consulta de Usuario')],
            [sg.Listbox(id, size= (50, 10), key='-BOX-')],
            [sg.Button('Excluir'),sg.Button('Alterar'),sg.Button('Adicionar'),sg.Button('Sair')]
         ]
window = sg.Window('Consulta', layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED,'Sair'):
        break
    if event == 'Excluir':
        if id:
            real = values['-BOX-'][0]
            x = (str(real[0]))
            back.delete(x)
            id = back.atualizar()
            window.find_element('-BOX-').update(id)
        