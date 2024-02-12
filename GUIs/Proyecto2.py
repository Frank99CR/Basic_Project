import PySimpleGUI as sg

sg.set_options(font=("Arial Bond", 20))

def main_window():

    layout = [
    [sg.Column([[sg.Text("Bienvenido a mis finanzas", size=(20, 1))]], justification="center")],
    [sg.Column([[sg.Button("Ingresos", size=(15,1))]], justification="center")],
    [sg.Column([[sg.Button("Gastos", size=(15,1))]], justification="center")],
    [sg.Column([[sg.Button("Salir", size=(15,1))]], justification="center")]
   ]
    return sg.Window("Mis finanzas", layout, size=(450,250))

def income_window():
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
    [sg.Button("Salir", key="-EXIT-")]
    ]
  return sg.Window("Ingresos", layout)


def expense_window():
    
  top_row_for_description_table = ['Titulo']
  rows_for_descriptions = []
  top_row_for_category_table = ['Categoria']
  rows_for_categories = []
  top_row_for_amount_table = ['Monto']
  rows_for_amounts = []
  dict_of_expenses = []

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
  return sg.Window("Gastos", layout)



# current_window = main_window()

def main_window_cycle():
 
 current_window = main_window()
 while True:
  event, values = current_window.read()

  if event == sg.WIN_CLOSED:
    break
  elif event == "Ingresos":
    current_window.hide()
    current_window = income_window()
  elif event == "Gastos":
    current_window.hide()
    current_window = expense_window()
  elif event == "Salir":
   break
 
 current_window.close()





main_window_cycle()



