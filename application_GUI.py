# pylint: disable=no-else-break
import PySimpleGUI as sg
import main_process as mp
import classificationABC as cls


file_instructions = cls.read_instructions("instructions.txt")
output_path = cls.get_folder_path("salida_abc")
input_path=cls.get_folder_path("entrada_abc")

layout = [
        [[sg.Text("PP nombre col. art.", justification="left", size=20), sg.InputText(default_text = 'ARTÍCULO', justification="left", size=20,key='-IN-PP-ART-'),sg.Text("Precio nombre col. art.", justification="left", size=19), sg.InputText(default_text = 'Artículo', justification="left", size=20,key='-IN-PRICE-ART') ],
        [sg.Text("PP nombre col. descrip.", justification="left", size=20), sg.InputText(default_text = 'DESCRIPCIÓN', justification="left", size=20,key='-IN-PP-DES-'),sg.Text("Precio nombre col. precio", justification="left", size=19), sg.InputText(default_text = 'Precio Neto + I. Internos', justification="left", size=20,key='-IN-PRICE-PRICE') ],
        [sg.Text("PP nombre col. VPD", justification="left", size=20), sg.InputText(default_text = 'VTA. PROMEDIO', justification="left", size=20,key='-IN-PP-VPD-')],
        [sg.Text("PP nombre col. stock", justification="left", size=20), sg.InputText(default_text = 'STOCK', justification="left", size=20,key='-IN-PP-STOCK-')],
    ],
    [
        sg.Text("Seleccionar Punto Pedido: ", justification="left", size=20),
        sg.Input(size=40, justification="left"),
        sg.FileBrowse(key="-IN-PP-", initial_folder = input_path),
    ],
    [
        sg.Text("Seleccionar Precio: ", justification="left", size=20),
        sg.Input(size=40, justification="left"),
        sg.FileBrowse(key="-IN-PRICE-",initial_folder = input_path ),
    ],

    # [
    #     sg.Text("Seleccionar Ruta output: ", justification="left", size=20),
    #     sg.Input(size=40, justification="left"),
    #     sg.FolderBrowse(key="-IN-OUT-",initial_folder = output_path ),
    # ],
    [sg.Button("Cargar archivos", key="-ADD-FILES-", size=12), sg.Button("Procesar", key="-PROCESS-FILES-",size=12)],
    [sg.Button('Salir', size=12)],
    [sg.Text("", key="-OUTPUT-")],
]

window = sg.Window("Clasificador ABC", layout)


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "-ADD-FILES-":
        file_path_pp = values["-IN-PP-"]
        file_path_price = values["-IN-PRICE-"]
        pp_art = values['-IN-PP-ART-']
        pp_des= values['-IN-PP-DES-']
        pp_vpd = values['-IN-PP-VPD-']
        pp_stock = values['-IN-PP-STOCK-']
        price_art = values['-IN-PRICE-ART']
        price_price = values['-IN-PRICE-PRICE']
        window["-OUTPUT-"].update("file with articles and price added")

    elif event == '-PROCESS-FILES-':
        df_stats, dictionary_abc, sin_stock = mp.main_process(file_path_pp,pp_art,pp_des,pp_vpd,pp_stock,file_path_price,price_art,price_price)
        #output_path = values["-IN-OUT-"]
        cls.export_excel(dictionary_abc,df_stats,sin_stock,file_instructions,output_path,"ABC_PROCESADO")
        sg.popup(f'ARCHIVOS PROCESADOS en carpeta:{output_path}')


    elif event == sg.WINDOW_CLOSED or event == 'Salir':
        break
    

window.close()
