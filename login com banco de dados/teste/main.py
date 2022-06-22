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

def validação():
    n_usuario = values['-USER-']
    pw_usuario = values['-PW-']
    back.dbase = sqlite3.connect('login.db')
    try:
        c = back.dbase.cursor()
        c.execute(f"SELECT usuario FROM login WHERE usuario ='{n_usuario}'")
        usuario_db = c.fetchall()  
        c.execute(f"SELECT senha FROM login WHERE usuario ='{n_usuario}'")
        senha_db = c.fetchall()
        if n_usuario == '' or pw_usuario == '':
            sg.popup('Usuario ou Senha vazio.',text_color= 'red')   
        elif n_usuario == usuario_db[0][0] and pw_usuario == senha_db[0][0]:
            sg.popup('Bem vindo ao sistema',text_color= 'green')  
    except:
            sg.popup('Usuario ou Senha invalida.',text_color= 'red')   


while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED,'Sair'):
        break
    if event == 'Entrar':
        validação()
        
