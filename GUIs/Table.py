import PySimpleGUI as sg
import json

sg.set_options(font=("Arial Bold", 14))

top_row_for_description_table = ['Titulo']
rows_for_descriptions = []
top_row_for_category_table = ['Categoria']
rows_for_categories = []
top_row_for_amount_table = ['Monto']
rows_for_amounts = []
dict_of_income = []

layout = [ 
    [sg.Column([[sg.Table(values=rows_for_categories, headings=top_row_for_category_table, auto_size_columns=False, display_row_numbers=False, justification='left', key='-TABLE_CATEGORY-', selected_row_colors=('red','yellow'), enable_events=True, expand_x=False, expand_y=True, enable_click_events=True)]], justification="left"),
     sg.Table(values=rows_for_descriptions, headings=top_row_for_description_table, auto_size_columns=True, display_row_numbers=False, justification='center', key='-TABLE_DESCRIPTION-', selected_row_colors=('red','yellow'), enable_events=True, expand_x=True, expand_y=False, enable_click_events=True),
     sg.Table(values=rows_for_amounts, headings=top_row_for_amount_table, auto_size_columns=True, display_row_numbers=False, justification='center', key='-TABLE_AMOUNT-', selected_row_colors=('red','yellow'), enable_events=True, expand_x=True, expand_y=False, enable_click_events=True),

    ],
    #[sg.Table(values=rows, headings=top_row, auto_size_columns=True, display_row_numbers=False, justification='center', key='-TABLE-', selected_row_colors=('red','yellow'), enable_events=True, expand_x=True, expand_y=False, enable_click_events=True)],
    # [sg.Table(values=rows2, headings=top_row2, auto_size_columns=False, display_row_numbers=False, justification='left', key='-TABLE-', selected_row_colors=('red','yellow'), enable_events=True, expand_x=False, expand_y=True, enable_click_events=True)],
    [sg.Text("Ingrese la categoria: ")],
    [sg.Input(key='-Categoria-')],
    [sg.Text("Ingrese la Descripcion: ")],
    [sg.Input(key='-Titulo-')],
    [sg.Text("Ingrese el monto: ")],
    [sg.Input(key='-Monto-')],
    [sg.Button('Agregar categoria', key="-submit_category-")],
    [sg.Button('Agregar descripcion', key="-submit_description-", disabled=True, tooltip='Primero debes ingresar una categoria')],
    [sg.Button('Agregar monto', key="-submit_amount-", disabled=True, tooltip='Primero debes ingresar una descripcion')],
    [sg.Button("Limpiar")],
    [sg.Button("Exportar", key="-EXPORT-")],
    # [sg.Button("Importar", key="-IMPORT-")]

]


def export_data_to_json(path):

  income_data_converted_to_json = json.dumps(data_dict, indent=4)
  with open (path, 'w') as file:
   file.writelines(income_data_converted_to_json)
  [sg.popup("Archivo Exportado exitosamente")]

def open_json_file(path):
    with open(path, 'r') as file:
        data = json.load(file)
    #print(data) 
    return data  

def import_data_from_json ():

  # list_with_data_from_income_table = open_json_file("Archivos/Ingresos")
  # new_row = list_with_data_from_income_table
  # rows.append(new_row)
  # window['-TABLE-'].update(values=rows)
  pass


   

window = sg.Window("Tabla", layout)


while True:
 event, values = window.read()

 if event == sg.WIN_CLOSED:
  break
 elif event == '-submit_category-':
  #new_row = [values['-Categoria-'], values['-Titulo-'], values['-Monto-']]
  new_row = [values['-Categoria-']]
  if values['-Categoria-'] == "":
   sg.popup("Debe ingresar una categoria ")
  else: 
   rows_for_categories.append(new_row)
   window['-TABLE_CATEGORY-'].update(values=rows_for_categories)
   window['-submit_description-'].update(disabled=False)

 elif event == '-submit_description-':
     new_row = [values['-Titulo-']]

     if values['-Titulo-'] == "":
       sg.popup("Debe ingresar una descripcion ")
     else: 
      rows_for_descriptions.append(new_row)
      window['-TABLE_DESCRIPTION-'].update(values=rows_for_descriptions)
      window['-submit_amount-'].update(disabled=False)
 elif event == '-submit_amount-':    
     new_row = [values['-Monto-']]

     if values['-Monto-'] == "":
       sg.popup("Debe ingresar un valor ")
     else: 
      rows_for_amounts.append(new_row)
      window['-TABLE_AMOUNT-'].update(values=rows_for_amounts)

      data_dict = {
       "Category" : rows_for_categories,
       "Description" : rows_for_descriptions,
       "Amount" :  rows_for_amounts,
   }
     dict_of_income.append(data_dict)




   
 elif event == "Limpiar":
  window['-Categoria-'].update("")
  window['-Titulo-'].update("")
  window['-Monto-'].update("") 
 elif event == '-EXPORT-':
  export_data_to_json("Archivos/Ingresos")
 elif event == '-IMPORT-':
   import_data_from_json() 

 


window.close()

