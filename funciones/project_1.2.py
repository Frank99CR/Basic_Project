import csv


def validation_of_score(user_score):
 while True:
  try:
    score = float(user_score)
    if score  < 0 or score < 100:
     return score
    else:
     print("Por favor, ingrese una nota válida.")
     user_score = input("Por favor, ingrese su nota nuevamente: ")
  except ValueError as error:
    print(f"Error: {error}")
  
  
def validates_numbers_in_name_and_last_name(user_name):
    while True:
     try:
       for char in user_name:
         if char.isdigit():
          print("El nombre no puede contener numeros. Recuerde que solo se aceptan letras")
          user_name = input("Ingrese el dato nuevamente: ")
          validates_numbers_in_name_and_last_name(user_name)
       else:
        return user_name
     except ValueError as error:
      print(f"Error: {error}")

     

def validation_of_group(user_group):
  while True:
    try:
      group = int(user_group)
      if group < 0  or group >10:
        return group
      else:
        print("Ingrese un grupo valido. Rango de 1 al 10")
        user_group = input("Ingrese el grupo nuevamente: ")
    except ValueError as error:
      print(f"Error: {error}")  
   

     
 
def register_student(list_of_students, student_headers, list_of_top_averages):
 

 name = validates_numbers_in_name_and_last_name(input("Please enter your name: "))
 last_name = validates_numbers_in_name_and_last_name(input("Please enter your last name: ")) 
 group = validation_of_group(input("Please enter your group: "))
 spanish_score = validation_of_score(input("Please enter your spanish score: "))
 science_score = validation_of_score(input("Please enter your science score: "))
 english_score = validation_of_score(input("Please enter your english score: "))
 sociology_score = validation_of_score(input("Please enter your sociology score: "))
       

 student_dict = {
    "name" : name,
    "last name" : last_name,
    "group" : group,
    "spanish score" : spanish_score,
    "science score" : science_score,
    "english score" : english_score,
    "sociology score" : sociology_score,
  }      
 list_of_students.append(student_dict)         
 print("Registro exitoso") 
 menu(list_of_students, student_headers, list_of_top_averages)
 return list_of_students


def print_list_of_students_registered(list_of_students, student_headers, list_of_top_averages):
   print("List of active students: ")
   print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
   for student in list_of_students:
     student_name = student.get("name")
     student_last_name = student.get("last name")
     student_group = student.get("group")
     print(f"Student: {student_name} {student_last_name}")
     print(f"Group: {student_group}")
     print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
   menu(list_of_students, student_headers, list_of_top_averages)  

def top_three_average_scores(list_of_students, student_headers, list_of_top_averages):

  
  for student in list_of_students:
    spanish_score = student.get("spanish score")
    science_score = student.get("science score")
    english_score = student.get("english score")
    sociology_score = student.get("sociology score")
    total_average =  (int(spanish_score) + int(english_score) + int(science_score) + int(sociology_score)) / 4
    list_of_top_averages.append(total_average)

  list_of_top_averages.sort(reverse=True)
  print (f"This is the top 3 scores: {list_of_top_averages [:3]}")
  menu(list_of_students, student_headers, list_of_top_averages)  

def total_average_of_scores(list_of_students, student_headers, list_of_top_averages):
    
    sum = 0

    for score in list_of_top_averages:
      sum = sum + score
    print(f"The average of notes is: {round(sum / len(list_of_students), 2)}")  
    menu(list_of_students, student_headers, list_of_top_averages)     
  

def export_to_csv(file_path, list_of_students, student_headers, list_of_top_averages):
  with open (file_path, 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=student_headers)
    writer.writeheader()
    writer.writerows(list_of_students)
    print("Archivos CSV creado exitosamente! ")  
  menu(list_of_students, student_headers, list_of_top_averages)  

def import_csv_file(file_path, list_of_students, student_headers, list_of_top_averages):
   with open (file_path, 'r') as file:
     reader = csv.DictReader(file)  
     for row in reader:
       print(row)
       list_of_students.append(row)
   menu(list_of_students, student_headers, list_of_top_averages)      
  

   
def menu(list_of_students, student_headers, list_of_top_averages):

  print("""    
    --------------------------------------------------
                  Project 1
    1) Registro de estudiantes
    2) Mostar estudiantes
    3) Ver mejores promedios
    4) Promedio total   
    5) Exportar a CSV
    6) Importar CSV  
    7) Salir             
    --------------------------------------------------

  """)

  user_input = input("Digite una opcion del menu: ")

  if user_input == "1":
    register_student(list_of_students, student_headers, list_of_top_averages)
  elif user_input == "2":
    print_list_of_students_registered(list_of_students, student_headers, list_of_top_averages)
  elif user_input == "3":
    top_three_average_scores(list_of_students, student_headers, list_of_top_averages)  
  elif user_input == "4":
    total_average_of_scores(list_of_students, student_headers, list_of_top_averages)
  elif user_input =="5":
    export_to_csv('students.csv', list_of_students, student_headers, list_of_top_averages)
  elif user_input == "6":
    import_csv_file('students.csv', list_of_students, student_headers, list_of_top_averages)
  elif user_input == "7": 
    print("Gracias por usar el sistema")
  else:
    print("Digite la opcion correcta ")
    menu(list_of_students, student_headers, list_of_top_averages)  



def entry_point():
  list_of_students = []
  list_of_top_averages = []
  student_headers = {
    "name",
    "last name",
    "group",
    "spanish score",
    "science score",
    "english score",
    "sociology score",
  }
  menu(list_of_students, student_headers, list_of_top_averages)    


entry_point()    


