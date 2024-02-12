import PySimpleGUI as sg

# Configuración global de opciones
sg.set_options(font=("Arial", 12))

# Crear botones
button_left = sg.Button('Izquierda', key='-LEFT-', size=(15, 1))
button_center = sg.Button('Centro', key='-CENTER-', size=(15, 1))
button_right = sg.Button('Derecha', key='-RIGHT-', size=(15, 1))

# Crear el diseño
layout = [
    [sg.Text('', size=(20, 1)), button_left, sg.Text('', size=(20, 1))],
    [sg.Text('', size=(20, 1)), button_center, sg.Text('', size=(20, 1))],
    [sg.Text('', size=(20, 1)), button_right, sg.Text('', size=(20, 1))],
]

# Crear la ventana
window = sg.Window("Botones Alineados", layout, size=(400, 200))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()
