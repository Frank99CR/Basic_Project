import operator
class Student:
  name : str
  last_name : str
  score : int

  def __init__(self, name, last_name, score):
   self.name = name
   self.last_name = last_name
   self.score = score

  def print_name(self):
   print(self.name)  


def entry_point():
  list_of_students = []
  menu(list_of_students)


def register_student(list_of_students):
  name = input("Please enter your name: ")
  last_name = input("Please enter your last name: ")
  score = float(input("Please enter your score: "))
  student1 = Student(name, last_name, score)
  student_dict = {
    "Name" : student1.name,
    "Last Name" : student1.last_name,
    "Score" : student1.score
  }
  list_of_students.append(student_dict)
  print("Registro exitoso")
  
  menu(list_of_students)

def get_list_of_students(list_of_students):
  for student in list_of_students:
    print(student)
  menu(list_of_students)  

def get_top_scores(list_of_students):
    
    print(sorted(list_of_students[0:3], key=operator.itemgetter('Score'), reverse=True))
    
    menu(list_of_students)

  


def get_average_of_scores(list_of_students):

  list_of_scores = []
  sum = 0
  
  for x in list_of_students:
    score = x.get("Score")
    list_of_scores.append(int(score))
  for score in list_of_scores:
    sum = sum + score

  final_average = sum / len(list_of_scores) 
  print(f"Average Score: {round(final_average, 2)}")   
  menu(list_of_students)


def menu(list_of_students):

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
    register_student(list_of_students)
  elif user_input == "2":
    get_list_of_students(list_of_students)
  elif user_input == "3":
    get_top_scores(list_of_students)  
  elif user_input == "4":
    get_average_of_scores(list_of_students)
  elif user_input == "5": 
    print("Gracias por usar el sistema")
  else:
    print("Digite la opcion correcta ")
    menu(list_of_students)  
    
  


entry_point()





 


