#Iteración directa
my_favorite_records = [
	'Dark Side Of The Moon',
	'Fear of a Blank Planet',
	'Signify',
]

#for record in my_favorite_records:
	#print(f'Record: {record}')

#Iteración por índice
my_favorite_records = [
	'Dark Side Of The Moon',
	'Fear of a Blank Planet',
	'Signify',
	
]

# for index in range(0, len(my_favorite_records)):
# 	record = my_favorite_records[index]
# 	print(f'Record {index}: {record}')


#Iteración directa incluyendo índice

my_favorite_records = [
	'Dark Side Of The Moon',
	'Fear of a Blank Planet',
	'Signify',
]

# for index, record in enumerate(my_favorite_records):
# 	print(f'Record {index}: {record}')

#Strings

my_string = 'Star Wars'

# for char in my_string:
# 	print(char)


#Ejercicio 1 ----->

first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]

for index, data_in_list in enumerate(first_list):
    data_in_second_list = second_list[index]
    #print(data_in_list, data_in_second_list)
	

#Ejercicio 2 ----->

my_string = "Pizza con piña"  

for char in range (len(my_string) -1, -1, -1): #-1 : Esto representa el índice del último carácter en la cadena my_string. Restamos 1 a la longitud de la cadena para obtener el índice del último carácter. / -1: Este es el valor de parada del rango. El bucle se ejecutará hasta que alcance este valor, pero no lo incluirá. En este caso, -1 es el índice del primer carácter en la cadena. Establecerlo en -1 significa que el bucle se detendrá antes de llegar al primer carácter, lo que nos permite iterar en sentido inverso. / -1:  Esto es el paso o incremento del rango. Indica cuánto se disminuirá el valor de la variable de iteración en cada paso del bucle. Establecerlo en -1 significa que el bucle irá retrocediendo desde el último índice hacia el primero.
    pass
	#print(my_string[char])

# for char in range(0, 1):
#     print(my_string[::-1])

    
    


# Manejo de listas

#Agregar datos

my_pets_list = [
	'dog',
	'cat',
]

my_pets_list.append('rabbit') #append
# print(my_pets_list)

courses_list = [
	'Computers',
	'Algorithms',
	'Python',
	'Web Development',
]

courses_list.insert(2, 'Databases')  #insert
# print(courses_list)


# Extend para unir 2 listas
first_list = [
	'A',
	'B',
	'C',
]

second_list = [
	'D',
	'E',
	'F',
]

first_list.extend(second_list) #Extend
# print(first_list)
# print(second_list)


#Eliminar datos

milky_way_planets = [
	'Mercury',
	'Venus',
	'Earth',
	'Mars',
	'Pluto',
	'Jupiter',
	'Saturn',
	'Uranus',
	'Neptune',
]

deleted_item = milky_way_planets.pop(4)  #Pop 
# print(milky_way_planets)
# print(f'Deleted item: {deleted_item}')


#Ejercicio 3 ----->

my_list = [4, 3, 6, 1, 7]

if my_list is not None:
    my_list[0], my_list[-1] = my_list[-1], my_list[0]
#print(my_list)    



#Ejercicio 4 ----->

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_pairs = []
for number in my_list:
    if number % 2 == 0:
        list_of_pairs.append(number)
#print(list_of_pairs)     


#Ejercicio 5 ---->

list_of_numbers = []
# for number_requested in range(0, 10):
#     number = int(input("Digite un numero: "))
#     list_of_numbers.append(number)
# max_value = max(list_of_numbers)    
# print(list_of_numbers) 
# print(f"The highest value is:  {max_value}")
    



#Ejercicio 6 ---->

hotel_diccionario = {
    "hotel" : {
        "nombre" : "Hilton inn",
        "Estrellas" : 4,
        "Numero de habitaciones" : 70
	},
    "Habitaciones" : {
        "Numero de habitacion" : 10,
        "Piso" : 4, 
        "Precio por noche" : 200
	}
    
    
}
# print(hotel_diccionario['hotel']['nombre'])
# print(hotel_diccionario['Habitaciones']['Precio por noche'])


# Ejercicio 7 ---->

list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]

for index, value_from_first_list in enumerate(list_a):
 value_from_second_list = list_b[index]
 my_dicctionary = {
     value_from_first_list : value_from_second_list 
 }
 #print(my_dicctionary) 


# Ejercicio 8 ---->

list_of_keys = ["access_level", "age"]
employee = {
    "name": "John",
	"email" : "john@ecorp.com",
 	"access_level": 5,
	"age" : 28
    }
 
        
# for key in list_of_keys:
#     if key in employee:
#      employee.pop(key)
#      print(f'Deleted item: {key}')
# #print(employee)

