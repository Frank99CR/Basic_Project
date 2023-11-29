
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





#inverted_bubble_sort(list2)


def inverted_bubble_sort_with_positive_index (list_to_sort): #Positive indexgit b
 
 for outer_index in range(len(list_to_sort)-1, -1, -1):

  for index in range(len(list_to_sort)-1, - 1, -1):
   has_made_changes = False
   current_element = list_to_sort [index]
   next_index = index - 1
   next_element = list_to_sort [index - 1]
   #print(f"Index: {index}, Current element: {current_element}, next element: {next_element}" 
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
  
     


list2 = [10,11,6,5,4,3,2,1]
    
inverted_bubble_sort_with_positive_index(list2)

