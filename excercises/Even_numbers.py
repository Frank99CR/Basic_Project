even_number = 0
for number in range (0, 101):
    if number % 2 == 0:
        even_number = even_number + number
print(even_number)        


total = 0

for number in range (2, 101, 2):
    total = total + number
print (total)    