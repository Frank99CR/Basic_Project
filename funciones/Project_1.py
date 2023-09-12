list_of_students = []
list_of_scores = []


def register_student():

  student_name = input("Please enter your name: ")
  student_last_name = input("Please enter your last name: ")
  student_score = float(input("Please enter your score: "))
  final_name = student_name +" "+ student_last_name
  list_of_students.append(final_name)
  list_of_scores.append(student_score)

  print("The student was sucessfully registered")
  
  menu()

def get_list_of_students(list_of_students, list_of_scores):
  
    for student in range(len(list_of_scores)):
      print(f"Name: {list_of_students[student]}, Score: {list_of_scores[student]}")

    menu()  
    
  
  

def get_top_scores(list_of_scores):
  top_three_scores = list_of_scores.copy()
  top_three_scores.sort(reverse=True)

  if len(top_three_scores) == 0:
   print("No scores available")
  else:
   for score in top_three_scores[0:3]:
    print(f"Nota: {score}")

  
  menu()


def get_average_of_scores(list_of_scores):
  sum_of_scores = 0
  for score in list_of_scores:
    sum_of_scores = sum_of_scores + score

  final_average = sum_of_scores / len(list_of_scores)  

  
  print(f"The average of all scores is: {round(final_average, 2)}")
  menu()





def menu():

  print("""    
    --------------------------------------------------
                  Project 1
    1) Student Record
    2) Show students records
    3) Show top averages
    4) Total average    
    5) Exit            
    --------------------------------------------------

  """)

  user_input = input("Please enter a menu option: ")

  if user_input == "1":
    register_student()
  elif user_input == "2":
    get_list_of_students(list_of_students, list_of_scores)
  elif user_input == "3":
    get_top_scores(list_of_scores)  
  elif user_input == "4":
    get_average_of_scores(list_of_scores)
  elif user_input == "5": 
    print("Thank you")
  else:
    print("Enter the correct option ")
    menu()  
    
  


menu()





 


