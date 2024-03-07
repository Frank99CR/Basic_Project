import PySimpleGUI as sg
import json

sg.set_options(font=("Arial Bond", 20))
# Diseño de las pestañas
tab1_layout = [
    [sg.Text('Registre las categorias')],
    [sg.InputText('', key='-categoria-')],
    [sg.Button('Ingresar', key="-submit-")]
]
rows = []
toprow = ["Categoria", "Descripcion", "Monto"]
list_of_categories = []
financial_data = []
financial_dict= {}


def export_data_to_json(path):

  income_data_converted_to_json = json.dumps(financial_data, indent=4)
  with open (path, 'w') as file:
   file.writelines(income_data_converted_to_json)
  [sg.popup("Archivo Exportado exitosamente")]



tab2_layout = [ 
        [sg.Table(values=rows, headings=toprow, auto_size_columns=True, display_row_numbers=False, justification='center', key='-TABLE-', selected_row_colors=('black on white'), enable_events=True, expand_x=True, expand_y=True, enable_click_events=True)],
        [sg.Combo(list_of_categories, key='-combo-', default_value="Seleccione una opcion", size=(20, 1))],
        [sg.InputText('Ingrese el titulo', key='-titulo-')],
        [sg.InputText('Ingrese el monto', key='-monto-')],
        [sg.Button('Ingresar', key='-ADD-')],
        [sg.Button('Limpiar', key='-CLEAR-')],
        [sg.Button('Exportar', key='-EXPORT-')]

]

#Diseño principal
layout = [
    [sg.TabGroup([
        [sg.Tab('Categorias', tab1_layout)],
        [sg.Tab('Movimientos', tab2_layout)]
    ])],
    [sg.Button('Salir')]
]

# Crear la ventana
window = sg.Window('Mis Finanzas', layout)



# Loop principal
while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Salir'):
        break
    elif event == '-submit-':
        new_category = values['-categoria-']
        if new_category in list_of_categories:
            sg.popup("La categoria ya existe")
        else:
            list_of_categories.append(new_category)
            sg.popup("Categoria registrada")
            print(list_of_categories)
            window['-combo-'].update(values=list_of_categories)
            window['-categoria-'].update("")
    elif event == '-CLEAR-':
      window['-combo-'].update("")
      window['-titulo-'].update("")
      window['-monto-'].update("")    
    elif event == '-ADD-':
      new_row = [values['-combo-'], values['-titulo-'], values['-monto-']]
      rows.append(new_row)
      if values ['-combo-'] not in list_of_categories:
         sg.popup("Categoria no registrada")
      else: 
        window['-TABLE-'].update(values=rows)
    elif event == '-EXPORT-':
       
       data_dict= {
            "Category" : values['-combo-'],
            "Description" : values['-titulo-'],
            "Amount" : values['-monto-'],
         }
       financial_data.append(data_dict)
       print(financial_data)
       export_data_to_json("Archivos/Ingresos")
          


window.close()
