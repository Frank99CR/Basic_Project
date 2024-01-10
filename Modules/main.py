from menu import user_menu

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
  user_menu(list_of_students, student_headers, list_of_top_averages)    
  

entry_point()


