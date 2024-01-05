from actions import register_student, print_list_of_students_registered, top_three_average_scores, total_average_of_scores
from data import import_csv_file, export_to_csv


def user_menu(list_of_students, student_headers, list_of_top_averages): 
 while True:
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
    break
  else:
    print("Digite la opcion correcta ")
    