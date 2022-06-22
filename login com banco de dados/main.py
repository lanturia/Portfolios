import sqlite3
import PySimpleGUI as sg
import back


sg.theme('Dark Amber') # Tema das janelas

# Layout da janela
layout = [
            [sg.Text('Login de Usuario')],
            [sg.Text('Login',size = (7,1), justification='left'),sg.InputText(key='-USER-', size = (20,1))],
            [sg.Text('Senha',size = (7,1), justification='left'),sg.InputText(key='-PW-', password_char="*", size =(20,1))],
            [sg.Button('Entrar'), sg.Button('Sair'), sg.Button('Cadastrar')]
        ]


# Criação da janela
window = sg.Window('Login', layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED,'Sair'):
        break
    if event == 'Entrar':
        n_usuario = values['-USER-']
        pw_usuario = values['-PW-']
        back.dbase = sqlite3.connect('login.db')
        c = back.dbase.cursor()   
    try:
        c.execute(f"SELECT senha FROM login WHERE usuario ='{n_usuario}'")
        senha_db = c.fetchall()
        back.dbase.close()
        if pw_usuario == senha_db[0][0]:
            sg.popup('Bem vindo ao sistema',text_color= 'green')
        else:
            sg.popup('Senha invalida.',text_color= 'red')
    except:
        sg.popup('Erro de validação do usuario.',text_color= 'red')
# window.close()
