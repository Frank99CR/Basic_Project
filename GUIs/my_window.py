import PySimpleGUI as sg

sg.set_options(font=("Arial Bond", 20))

top_row = ['Categoria', 'Titulo', 'Monto']
rows = []

# Declarar los elementoss
layout = [
    [sg.Column([[sg.Text("Bienvenido a mis finanzas", size=(20, 1))]], justification="center")],
    #[sg.Text(counter, key="-COUNTER-")],
    [sg.Column([[sg.Button("Ingresos", size=(15,1))]], justification="center")],
    [sg.Column([[sg.Button("Gastos", size=(15,1))]], justification="center")],
    [sg.Column([[sg.Button("Salir", size=(15,1))]], justification="center")]
    #[sg.Button("Ingresos", size=(15,1))], 
    #[sg.Button("Gastos", size=(15,1))],
]
income_layout = [
    [sg.Table(values=rows, headings=top_row, auto_size_columns=True, display_row_numbers=False, justification='center', key='-TABLE-', selected_row_colors=('red','yellow'), enable_events=True, expand_x=True, expand_y=False, enable_click_events=True)],
    [sg.InputText('', key='-CATEGORIA-')],
    [sg.InputText('', key='-TITULO-')],
    [sg.InputText('', key='-MONTO-')],
    [sg.Column([[sg.Button('Agregar ingreso', key='-ADD-', size=(20,1))]])],
    [sg.Column([[sg.Button('Exportar Data', key='-EXPORT-', size=(20,1))]])],
    [sg.Column([[sg.Button('Salir', size=(20,1))]])]
]
expense_layout = [
    [sg.Table(values=rows, headings=top_row, auto_size_columns=True, display_row_numbers=False, justification='center', key='-TABLE-', selected_row_colors=('red','yellow'), enable_events=True, expand_x=True, expand_y=False, enable_click_events=True)],
    [sg.InputText('', key='-CATEGORIA-')],
    [sg.InputText('', key='-TITULO-')],
    [sg.InputText('', key='-MONTO-')],
    [sg.Column([[sg.Button('Agregar Gasto', key='-ADD-', size=(20,1))]])],
    [sg.Column([[sg.Button('Exportar Data', key='-EXPORT-', size=(20,1))]])],
    [sg.Column([[sg.Button('Salir', size=(20,1))]])]
]

def calling_income_window():
 income_window = sg.Window("Ingresos", income_layout, size=(715, 700), resizable=True)

 while True:
    income_event, income_values = income_window.read()
    if income_event == sg.WIN_CLOSED:
        break
    elif income_event == "Salir":
       break
 income_window.close()

def calling_expense_window():
 expense_window = sg.Window("Gastos", expense_layout, size=(715, 700), resizable=True)

 while True:
    expense_event, expense_values = expense_window.read()
    if expense_event == sg.WIN_CLOSED:
        break
    elif expense_event == "Salir":
       break
 expense_window.close() 

# Crear la ventana
window = sg.Window("Mis finanzas", layout, size=(450,250))

# Event Loop para procesar "events" y obtener los "values" de los inputs
while True:
    event, values = window.read()
    # Procesar el evento del cerrar la ventaja
    # (si el usuario lo hace)
    if event == sg.WIN_CLOSED:
        break
    elif event == "Ingresos":
        calling_income_window()
        pass
    elif event == "Gastos":
        calling_expense_window()
    elif event == "Salir":
       break

    #window["-COUNTER-"].update(counter)

window.close()

