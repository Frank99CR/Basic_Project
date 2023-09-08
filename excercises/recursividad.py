def cuenta_atras(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_atras(numero)
    else:
        print("Hola")    

#cuenta_atras(12)


#Revisar imprimir hola -> ejemplo de recursividad
def imprimir_hola(palabra, contador):
    if contador <= 10:
      print("hola")
      imprimir_hola(palabra,  contador + 1)
    

#imprimir_hola("hola", 34)

#numero = 12

#print(f"Hola {numero}")

def imprimir_hola(numero, contador):
    if contador <= 10:
      print(numero)
      imprimir_hola(numero, contador + 1)
    

#imprimir_hola(1, 0)