
def inverted_bubble_sort (list_to_sort): #Negative Index
 for outer_index in range(-1, -len(list_to_sort), -1):
  for index in range (-1, -len(list_to_sort),- 1):
   #print(f"Index: {index}, elemento: {list_uno [index]}")
   has_made_changes = False
   current_element = list_to_sort [index]
   next_index = index - 1
   next_element = list_to_sort [index - 1]
   #print(f"Index: {outer_index},{index}, elemento: {current_element}, siguiente elemento: {list_uno [next_element]}")
   if next_index >= -len(list_to_sort):
    print(f"Iteracion:{outer_index},{index} Elemento actual: {current_element}, Siguiente Elemento: {next_element}")
            
    if current_element < next_element:
     print('El elemento actual es menor al siguiente. Intercambiandolos...')
     list_to_sort [index] = next_element
     list_to_sort[index -1] = current_element
     has_made_changes = True
     print(list_to_sort)
 if not has_made_changes:
     return  




def inverted_bubble_sort_with_positive_index (list_to_sort): #Positive index
 
 for outer_index in range(0, len(list_to_sort)):

  for index in range(len(list_to_sort)-1 , - 1 + outer_index, -1):
   has_made_changes = False
   current_element = list_to_sort [index]
   next_index = index - 1
   next_element = list_to_sort [index - 1]
   #print(f"Index: {index}, Current element: {current_element}, next element: {next_element}")
   if next_index != -1:
    print(f"Iteracion:{outer_index}.{index} Elemento actual: {current_element}, Siguiente Elemento: {next_element}")
   else: 
    next_element = 0
    print(f"Iteracion:{outer_index}.{index} Elemento actual: {current_element}, Siguiente Elemento: None") 

   if current_element < next_element:
    print('El elemento actual es menor al siguiente. Intercambiandolos...')
    list_to_sort [index] = next_element
    list_to_sort[index -1] = current_element
    print(list_to_sort)
    has_made_changes = True
    
 if not has_made_changes:
     return 
  


def bubble_sort(list_to_sort):
	# Repetimos la iteración de la lista por todos los elementos para moverlos al final
  for outer_index in range(0, len(list_to_sort) - 1):
    # Usamos esta variable para revisar si hemos movido elementos
    has_made_changes = False
		# Le restamos uno al length para parar en el penultimo elemento
    # Usamos el indice exterior para restar las ejecuciones de
    # los elementos que ya estan ordenados al final
    for index in range(0, len(list_to_sort) - 1 - outer_index):
      # Guardamos los valores del elemento actual y el siguiente
      current_element = list_to_sort[index]
      next_element = list_to_sort[index + 1]

      print(f'-- Iteracion {outer_index}, {index}. Elemento actual: {current_element}, Siguiente elemento: {next_element}')

      # Si el actual es mayor al siguiente, intercambiamos sus posiciones
      if current_element > next_element:
        print('El elemento actual es mayor al siguiente. Intercambiandolos...')
        list_to_sort[index] = next_element
        list_to_sort[index + 1] = current_element
        has_made_changes = True

    # Si no hemos movido elementos, la lista ya esta ordenada
    if not has_made_changes:
      return
    
  return list_to_sort  



     


list2 = [10,11,6,5,4,3,2,1]
    
#inverted_bubble_sort_with_positive_index(list2)
bubble_sort(list2)
print(list2)

#inverted_bubble_sort(list2)

