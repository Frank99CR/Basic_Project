import json

def open_json_file(path):
    with open(path, 'r') as file:
        data = json.load(file)
    print(data)  
    return data 


#open_json_file('Archivos/pokemon.json')


def add_pokemon_to_json_file(path):

    list_of_pokemon = open_json_file('Archivos/pokemon.json')

    pokemon_name = input("Please enter your pokemon name: ")
    pokemon_type = input("Please enter the type: ")
    pokemon_hp = int(input("Please enter your pokemon HP: "))
    pokemon_attack = int(input("Please enter your pokemon attack stat: "))
    pokemon_defense = int(input("Please enter your pokemon defense stat: "))
    pokemon_speed_attack = int(input("Please enter your pokemon speed attack stat: "))
    pokemon_speed_defense = int(input("Please enter your pokemon speed defense stat: "))
    pokemon_speed = int(input("Please enter your pokemon speed stat: "))

    pokemon_dict = {
        "name": {
        "english": pokemon_name
      },
      "type": [
        pokemon_type
      ],
      "base": {
        "HP": pokemon_hp,
        "Attack": pokemon_attack,
        "Defense": pokemon_defense,
        "Sp. Attack": pokemon_speed_attack,
        "Sp. Defense": pokemon_speed_defense,
        "Speed": pokemon_speed
      }

    }
    list_of_pokemon.append(pokemon_dict)
    list_of_pokemon_converted_to_json = json.dumps(list_of_pokemon, indent=4)

    
   
    with open(path, 'w') as file:
         file.writelines(list_of_pokemon_converted_to_json)

add_pokemon_to_json_file('Archivos/pokemon.json')    