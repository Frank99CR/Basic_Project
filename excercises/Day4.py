#Randomisation and Lists
import random
#import turtle_1 # puedo importar funciones, librerias o informacion de otros archivos con el import 

random_integer = random.randint(1, 5)    
print(random_integer)

#random_float = random.random() * 5

#print(random_float)


#Lists 


fruits = ["Manzana", "Banano", "Limon", "Fresas"]
vegetables = ["Papas", "Espinacas", "Rabano"]

#fruits[2] = "Lemon" # asigno un nuevo data al index 2 de la lista / las listas siempre empiezan de 0 

fruits.append("Aguacate") #append -> me agrega un valor o dato al final de la lista

#new_fruit = input(print("Dame una nueva fruta"))

#fruits.append(new_fruit)

#fruits.extend(["Provincias", "Alajuela", "San Jose", "Cartago"]) #-> extend me agrega una lista or a bunch of data to my previous list

# https://docs.python.org/3/tutorial/datastructures.html / More information 

#print(fruits)

#nested list / list within a list


total_list = [fruits, vegetables] #list within a list / total list contains list of fruist and vegetables

print(total_list)


