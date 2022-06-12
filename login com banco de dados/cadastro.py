import PySimpleGUI as sg
import back


sg.theme('Dark Amber') # Tema das janelas

cadastro = [
            [sg.Text('Cadastro de Usuario')],
            [sg.Text('Login',size = (7,1), justification='left'),sg.InputText(key='-LOGIN-', size = (20,1))],
            [sg.Text('Senha',size = (7,1), justification='left'),sg.InputText(key='-SENHA-', size =(20,1))],
            [sg.Button('Salvar'), sg.Button('Voltar')]
        ]

window = sg.Window('Cadastro', cadastro)

while True:
    event, values = window.read()
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
    if event in (sg.WINDOW_CLOSED,'Voltar'):
        break
window.close()