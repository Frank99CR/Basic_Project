import PySimpleGUI as psg
import json

psg.set_options(font=("Arial Bold", 14))

toprow = ['Categoria', 'Titulo', 'Monto']
rows = []

tbl1 = psg.Table(values=rows, headings=toprow,
                 auto_size_columns=True,
                 display_row_numbers=False,
                 justification='center', key='-TABLE-',
                 selected_row_colors=('black on white'),
                 enable_events=True,
                 expand_x=True,
                 expand_y=True,
                 enable_click_events=True)

add_text = psg.InputText('Ingrese la categoria', key='-categoria-')
add_titulo = psg.InputText('Ingrese el titulo', key='-titulo-')
add_monto = psg.InputText('Ingrese el monto', key='-monto-')
add_button = psg.Button('Add Row', key='-ADD-')
delete_button = psg.Button('Delete row', key='-DELETE-')
export_button = psg.Button('Export to file', key='-EXPORT-')


layout = [[tbl1], [add_button], [delete_button], [export_button], [add_text], [add_titulo], [add_monto]]

window = psg.Window("Ingresos", layout, size=(715, 700), resizable=True)

def add_row():
    new_row = [values['-categoria-'], values['-titulo-'], values['-monto-']]  # Initialize a new row with default values
    rows.append(new_row)
    window['-TABLE-'].update(values=rows)

def delete_row():
    rows.pop(values
             )
    window['-TABLE-'].update(values=rows)

def export_to_json():
    data_to_export = {
    "toprow": toprow,
    "row":rows
    }
    converted_value = json.dumps(data_to_export)
    print(converted_value)

while True:
    event, values = window.read()

    if event == psg.WIN_CLOSED:
        break
    elif event == '-TABLE-':
        # Handle table row click event
        if values['-TABLE-']:
            
            psg.popup("You clicked row: {}".format(values['-TABLE-'][0]))
            #window['-TABLE-'].update(values=rows)

    elif event == '-ADD-':
        # Handle add row button click event
        add_row()
        #window['-TABLE-'].update(values=rows)
    elif event == '-DELETE-':
        delete_row()   
    elif event =='EXPORT':
        export_to_json()

window.close()




#import PySimpleGUI as sg

# # Datos de ejemplo (una lista de diccionarios)
# table_data = [
#     {'Name': 'John', 'Age': 25, 'Country': 'USA'},
#     {'Name': 'Alice', 'Age': 30, 'Country': 'Canada'},
#     {'Name': 'Bob', 'Age': 22, 'Country': 'UK'}
# ]

# # Definir encabezados de columna
# headers = list(table_data[1].keys())

# # Crear el diseño de la interfaz gráfica con sg.Table
# layout = [
#     [sg.Table(values=table_data, headings=headers, auto_size_columns=False,
#               justification='right', display_row_numbers=False, num_rows=min(25, len(table_data)))]
# ]

# # Crear la ventana
# window = sg.Window('PySimpleGUI con Diccionarios', layout)

# # Loop principal para manejar eventos
# while True:
#     event, values = window.read()

#     if event == sg.WINDOW_CLOSED:
#         break

# # Cerrar la ventana al salir del loop principal
# window.close()
