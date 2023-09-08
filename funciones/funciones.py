import math

def sum (number1, number2):
    print(number1 + number2)

#sum(2, 3)    

def division (number1, number2):
    print(round(number1 / number2))

#division(20, 5)   

def multiply (number1, number2):
    print(number1 * number2)

#multiply (9, 9)   


def hello ():
    print("Hello")
    world()

def world():
    print("world")

#hello()

def word ():
    name = "Valeria"
    print(name)

#word()
#print(name)

card_balance = 200

def card_payment():
    print(card_balance)

#card_payment()

def get_max_of_two_numbers(number1, number2):
    if number1 > number2:
        return number1
    
    return number2

#print(get_max_of_two_numbers (49, 46))    

list = [4,6,2,29]

def sum_of_a_list (list):
    sum = 0
    for number in list:
        sum += number
    print(sum)

#sum_of_a_list (list)



def get_upper_and_lower_cases (word):
    counter_upper_cases = 0
    counter_lower_cases = 0 

    for char in word:
        if char.isupper():
            counter_upper_cases += + 1
        elif char.islower():
            counter_lower_cases += + 1   
    return f"There's {counter_upper_cases} upper cases and {counter_lower_cases} lower cases"          



#print(get_upper_and_lower_cases ("I love Nacion Sushi")) 


def inverted_word(word): #not completed / Investigar slicing en python
    list = []
    final_string = ""

    for char in word:
        list.append(char)
        

    for character in list:  
        final_string += character 
    return final_string [:: -1]  


     
     
#print(inverted_word ("Hola mundo"))



#suggested data: "python", "variable", "funcion", "computadora", "monitor"

# user_list = input(print("Ingrese una lista separada por guiones: "))
# my_list = [user_list] 
my_list = ["Python", "Variable", "Funcion", "Computadora", "Monitor"] 

list = "python-variable-funcion-computadora-monitor"



#print(my_list)

def get_alphabetical_order (separeted_word): # reglas de ordenamiento lexicográfico estándar de Python, que trata las letras mayúsculas y minúsculas de manera diferente
    final_list = []
    separated_list = separeted_word.split("-")

    for char in separated_list:
        if char.isupper():
            char = char.lower() #
        final_list.append(char)
        final_list.sort()

    join_list = "-".join(final_list)    

    return join_list


      
#print(get_alphabetical_order("palabra-San Jose-Perez-Cartago"))   

def is_prime(number_to_check):
    
    if number_to_check <= 1:

        return False
    

    for divisor in range(2, int(math.sqrt(number_to_check)) + 1):
        if number_to_check % divisor == 0:
            return False

    return True
    



    
            
#print(is_prime(11))  
# print(is_prime(5))  
# print(is_prime(7))  
# print(is_prime(89))   
            
numbers_to_check = [1, 4, 5, 6, 7, 13, 9, 67, 69]           

def get_prime_number (list_of_numbers):

    list_of_primes =[]

    for number_to_check in list_of_numbers:
        if is_prime(number_to_check):
            list_of_primes.append(number_to_check)

    return list_of_primes  


print(get_prime_number(numbers_to_check))

