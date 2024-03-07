
import csv

def export_to_csv(file_path, list_of_students, student_headers, list_of_top_averages):
  with open (file_path, 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=student_headers)
    writer.writeheader()
    writer.writerows(list_of_students)
    print("Archivos CSV creado exitosamente! ")  
  #user_menu(list_of_students, student_headers, list_of_top_averages)  

def import_csv_file(file_path, list_of_students, student_headers, list_of_top_averages):
   with open (file_path, 'r') as file:
     reader = csv.DictReader(file)  
     for row in reader:
       print(row)
       list_of_students.append(row)
   #user_menu(list_of_students, student_headers, list_of_top_averages)  