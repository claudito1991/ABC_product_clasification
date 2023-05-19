# pylint: disable=no-else-break
import PySimpleGUI as sg
import main_process as mp
layout = [
    [sg.Text("Seleccionar Punto Pedido: ",justification='left', size=20), sg.Input(size=40,justification='left' ), sg.FileBrowse(key="-IN-PP-")],
    [sg.Text("Seleccionar Precio: ",justification='left',size=20), sg.Input(size=40,justification='left'), sg.FileBrowse(key="-IN-PRICE-")],[sg.Button("Procesar",key="-ADD-FILES-")],
    [sg.Text('', key='-OUTPUT-')]
]

window = sg.Window('Ventana con TextBox y Botón', layout)




while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-ADD-FILES-':
        file_path_pp = values['-IN-PP-']
        file_path_price = values['-IN-PRICE-']
        window['-OUTPUT-'].update("file with articles and price added")
        #sg.popup('main file added:', file_path_pp)

window.close()
