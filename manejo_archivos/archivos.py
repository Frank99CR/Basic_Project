
def open_and_print_file(path):
	file = open(path)
	print(file.read())

#open_and_print_file('hello.txt')


def open_and_print_file(path):
	with open(path) as file:
		print(file.read())

	print("La variable 'file' ya no existe")
	print('El archivo ya no esta abierto')

#open_and_print_file('Archivos/hello.txt')

from datetime import datetime


def generate_time_log():
  current_time = datetime.now()
  return 'Esto fue escrito a las ' + current_time.strftime('%I:%M %p')

def write_time_log_to_file(file_path):
  log = generate_time_log()
  with open(file_path, 'a') as file:
    file.write(log)

write_time_log_to_file('Archivos/time_entries.log')

# Ejercicio 1 ---> (A)


def read_songs_from_file(path):
  with open (path, 'r') as file:
    songs = file.readlines()
    for track in songs:
      print(f"Song: {track.strip()}") 
    songs.sort()
    
  return songs
    
                 

def write_sorted_songs_from_previous_file(path, new_path):
    music_tracks = read_songs_from_file(path)
    with open(new_path, 'w') as file:
       file.writelines(music_tracks)
        

#read_songs_from_file("Archivos/canciones.txt")
#write_sorted_songs_from_previous_file('Archivos/canciones.txt', 'Archivos/canciones_ordenadas.txt')


# Ejercicio 1 ---> (B) Tabla (Excel)










