import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

final_password = ""

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


letter_string = ""
for letter in letters:
 letter = random.choices(letters, k=nr_letters)
letter_string += str(letter)


#random_integer = random.randint(0, nr_letters)    


# for x in range(nr_letters):
#  for letter in letters:
#   letter = letters[0]
# print(letter)






number_string = ""
for number in numbers:
  number = random.choices(numbers, k=nr_numbers)
number_string += str(number)
    

symbol_string = ""
for symbol in range (0, nr_symbols):
 symbol = random.choices(symbols, k=nr_symbols)
symbol_string = symbol_string + str(symbol)


my_password = []
my_password = my_password + str(letter_string) + str(symbol_string) + str(number_string) 




my_password.append(symbol_string)
my_password.append(letter_string)
my_password.append(number_string)

final_string = ""
for password in my_password:
  final_string = final_string + password
 

# print(letter_string)
# print(number_string)
# print(symbol_string)
   

print(f"Here is your password: {final_string}")


  
