import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_of_items = len(names) #cantidad de elementos de una lista

random_choice = random.randint(0, num_of_items - 1) # -1 porque se cuentan los index

person_who_will_pay = names[random_choice]

print(person_who_will_pay + f" is going to buy the meal today!")


#print(names[random.randint(0, end_of_list - 1)] + f" is going to buy the meal today!")


# Fran, Isa, Luis, Sebas, Jos, Emily, Angela, Jack, Chloe, Jenny, Ben



