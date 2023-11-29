def bubble_sort(list_to_sort):

 for outer_index in range (len(list_to_sort) -1):
   for index in range (0, len(list_to_sort)- 1 - outer_index):
    has_made_changes = False
  
    current_element = list_to_sort[index]
    next_element = list_to_sort[index + 1]
    print(f"Iteracion:{outer_index}.{index} Elemento actual: {current_element}, Siguiente Elemento: {next_element}")

    if current_element > next_element:
     print('El elemento actual es mayor al siguiente. Intercambiandolos...')
     list_to_sort[index] = next_element
     list_to_sort [index + 1] =  current_element
     has_made_changes = True
     print(list_to_sort)

 if not has_made_changes:
  return


#list1 = [10,3,5,18,6,2,4,1]
list2 = [10,11,6,5,4,3,2,1]


bubble_sort(list2)

