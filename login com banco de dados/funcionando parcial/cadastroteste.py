import PySimpleGUI as sg
import back


sg.theme('Dark Amber') # Tema das janelas   

id = back.atualizar()
login = back.atualizar()

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
    if event == 'Alterar':
            real = values['-BOX-'][0]
            x = (str(real[0]))
            y = (str(real[1]))
            z = (str(real[2]))
            back.alterar(x,y,z)
            id = back.atualizar()
            window.find_element('-BOX-').update(id)


