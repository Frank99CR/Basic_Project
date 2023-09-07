list_of_students = []
list_of_scores = []
top_score_student = []

def register_student():
  name = input("Please enter your name: ")
  last_name = input("Please enter your last name: ")
  score_per_student = float(input("Please enter your score: "))
  final_name = name +" "+ last_name
  list_of_students.append(final_name)
  list_of_scores.append(score_per_student)

  print("Registro exitoso")
  
  menu()

def get_list_of_students(list_of_students, list_of_scores):
  for student in list_of_students:
    for score in list_of_scores:
      print(f"Name:{student}: Score:{score}")

  menu()  

def get_top_scores(list_of_scores):
  top_three_student = []
  for best_score in list_of_scores:
    top_three_student.append(best_score)
  top_three_student.sort()    
  print(top_three_student)
  menu()


def get_average_of_scores(list_of_scores):
  sum_of_scores = 0
  for scores in list_of_scores:
    sum_of_scores = sum_of_scores + scores

  final_average = sum_of_scores / len(list_of_scores)  

  print(round(final_average, 2))
  menu()





def menu():

  print("""    
    --------------------------------------------------
                  Project 1
    1) Registro de estudiantes
    2) Mostar estudiantes
    3) Ver mejores promedios
    4) Promedio total    
    5) Salir             
    --------------------------------------------------

  """)

  user_input = input("Digite una opcion del menu: ")

  if user_input == "1":
    register_student()
  elif user_input == "2":
    get_list_of_students(list_of_students, list_of_scores)
  elif user_input == "3":
    get_top_scores(list_of_scores)  
  elif user_input == "4":
    get_average_of_scores(list_of_scores)
  elif user_input == "5": 
    print("Gracias por usar el sistema")
  else:
    print("Digite la opcion correcta ")
    menu()  
    
  


menu()





 


