import csv

# videogames = [{
#     'Nombre' : 'Final Fantasy 7',
#     'Género' : 'JRPG',
#     'Desarrollador' : 'Square Enix',
#     'Clasificación ESRB' : 'T'
# },
# {
#     'Nombre' : 'Pokemon Platinum',
#     'Género' : 'JRPG',
#     'Desarrollador' : 'Game Freak',
#     'Clasificación ESRB' : 'E'

# }
# ]

# def write_csv_file(file_path, data, headers):
#     with open(file_path, 'w', encoding='utf-8') as file:
#         writer = csv.DictWriter(file, headers)
#         writer.writeheader()
#         writer.writerows(data)

# #write_csv_file('videogame_list.csv', videogames, videogames[0].keys())    

# list_of_videogames = []
# videogame_headers = {
#         'name',
#         'genre',
#         'developer',
#         'rating'
#     }    

# def adding_games_to_dict(file_path, data, headers):

    
#     for _ in range(1):
#         dict_of_games = {}

#         name_key = input("Digite el key_name: ")
#         game_name = input("Digite el nombre del juego: ")
#         genre_key = input("Digite el key_genre: ")
#         genre = input("Digite el genero del juego: ")
#         developer_key = input("Digite el developer_key: ")
#         developer = input("Digite el desarrollador del juego: ")
#         rating_key = input("Ingrese el rating_key: ")
#         rating = input("Ingrese el rating ESRB del juego: ")
#         dict_of_games[name_key] = game_name
#         dict_of_games[genre_key] = genre
#         dict_of_games[developer_key] = developer
#         dict_of_games[rating_key] = rating

#         list_of_videogames.append(dict_of_games)


#     with open (file_path, 'w', encoding='utf-8') as file:
#         writer = csv.DictWriter(file, headers)
#         writer.writeheader()
#         writer.writerows(data)    

        

# adding_games_to_dict('videogames_list.csv', list_of_videogames, videogame_headers) # No puedo usar variables globales


def entry_point():
  list_of_videogames = []
  videogame_headers = {
         'name',
         'genre',
         'developer',
         'rating'
     }   
  menu(list_of_videogames, videogame_headers)

def register_videogame(list_of_videogames, videogame_headers):
  videogame_name = input("Please enter your video game: ")
  videogame_genre = input("Please enter your genre: ")
  developer = input("Please enter your game developer: ")
  videogame_rating = input("Please enter your game ESRB Rating: ")

  videogames_dict = {
    "name" : videogame_name,
    "genre" : videogame_genre,
    "developer" : developer,
    "rating" : videogame_rating,
  }
  list_of_videogames.append(videogames_dict)
  print("Registro exitoso")
  
  menu(list_of_videogames, videogame_headers)  

def get_list_of_videogames(list_of_videogames, videogame_headers):
  for game in list_of_videogames:
    print(game)
  menu(list_of_videogames, videogame_headers)    

def export_videogames_to_csv_file(file_path, list_of_videogames, videogame_headers):
  with open (file_path, 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, videogame_headers, dialect='excel-tab') #dialect='excel-tab')
    writer.writeheader()
    writer.writerows(list_of_videogames)
  print("Archivos CSV creado exitosamente! ")  
  menu(list_of_videogames, videogame_headers)  


def menu(list_of_videogames, videogame_headers):

  print("""    
    --------------------------------------------------
                  CSV File 
    1) Registro de video juegos
    2) Mostar video juegos
    3) Exportar a CSV
    4) Salir                
    --------------------------------------------------

  """)

  user_input = input("Digite una opcion del menu: ")

  if user_input == "1":
    pass
    register_videogame(list_of_videogames, videogame_headers)
  elif user_input == "2":
    get_list_of_videogames(list_of_videogames,videogame_headers)
  elif user_input == "3":
    export_videogames_to_csv_file('videogames.csv', list_of_videogames,  videogame_headers) 
  elif user_input == "4":
    print("Gracias por usar el sistema")
  else:
    print("Digite la opcion correcta ")
    menu(list_of_videogames, videogame_headers)  
    



entry_point()