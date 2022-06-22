import sqlite3
import PySimpleGUI as sg
import back

""" def validação():
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
            sg.popup('Usuario ou Senha invalida.',text_color= 'red')   """

def acesso():
    sg.theme('Dark Amber') # Tema das janelas
    # Layout da janela
    layout = [
                [sg.Text('Login de Usuario')],
                [sg.Text('Login',size = (7,1), justification='left'),sg.InputText(key='-USER-', size = (20,1))],
                [sg.Text('Senha',size = (7,1), justification='left'),sg.InputText(key='-PW-', password_char="*", size =(20,1))],
                [sg.Button('Entrar'), sg.Button('Sair'), sg.Button('Cadastrar')]
            ]
    # Criação da janela
    return sg.Window('Login', layout=layout, finalize= True)

def cadastro_usuario():
    sg.theme('Dark Amber') # Tema das janelas
    layout = [
                [sg.Text('Cadastro de Usuario')],
                [sg.Text('Login',size = (7,1), justification='left'),sg.InputText(key='-LOGIN-', size = (20,1))],
                [sg.Text('Senha',size = (7,1), justification='left'),sg.InputText(key='-SENHA-', size =(20,1))],
                [sg.Button('Salvar'), sg.Button('Voltar')]
             ]
    # Criação da janela
    return sg.Window('Cadastro', layout=layout, finalize= True)

def consulta_dados():
    sg.theme('Dark Amber') # Tema das janelas   
    
    id = back.atualizar()
    login = back.atualizar()

    layout = [
            [sg.Text('Consulta de Usuario')],
            [sg.Listbox(id, size= (50, 10), key='-BOX-')],
            [sg.Button('Excluir'),sg.Button('Alterar'),sg.Button('Adicionar'),sg.Button('Sair')]
             ]
    return sg.Window('Consulta', layout=layout, finalize= True)

janela1,janela2,janela3 = acesso(), None, None

# Inicio da logica

while True:
    window, event, values = sg.read_all_windows()

# Fechamento de janelas

    if window == janela1 and event in (sg.WINDOW_CLOSED,'Sair'):
        break
    if window == janela2 and event == sg.WINDOW_CLOSED:
        break
    if window == janela3 and event in (sg.WINDOW_CLOSED,'Sair'):
        break

# Login de sistema com consulta ao banco de dados    

    if event == 'Entrar':
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
                janela1.hide()
                janela3 = consulta_dados()
        except:
                sg.popup('Usuario ou Senha invalida.',text_color= 'red')  


# Botão de cadastro de usuario

    if window == janela1 and event == 'Cadastrar':
        janela1.hide()
        janela2 = cadastro_usuario()

    if window == janela3 and event == 'Adicionar':
        janela2 = cadastro_usuario()

# Botão de retorno a janela de login

    if window == janela2 and event =='Voltar':
        janela2.hide()
        janela1.un_hide()

# Sistema de cadastro de usuario

    if event == 'Salvar':
        usuario = values['-LOGIN-']
        senha = values['-SENHA-']
        if usuario and senha != '':
            back.cadastro(usuario, senha)
            window.find_element('-LOGIN-').update('')
            window.find_element('-SENHA-').update('')
            sg.popup('Login cadastrado com sucesso.',text_color= 'green')
        else:
            sg.popup('Erro, Senha ou Login vazios',text_color= 'red')


    if event == 'Excluir':
        if id:
            real = values['-BOX-'][0]
            x = (str(real[0]))
            back.delete(x)
            id = back.atualizar()
            window.find_element('-BOX-').update(id)
            
    if event == 'Alterar':
            real = values['-BOX-'][0]
            x = (str(real[0]))
            y = (str(real[1]))
            z = (str(real[2]))
            back.alterar(x,y,z)
            id = back.atualizar()
            window.find_element('-BOX-').update(id)