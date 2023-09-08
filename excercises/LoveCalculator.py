# Logical Operartors

# and / not 

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = combined_string.count('t')
r = combined_string.count('r')
u = combined_string.count('u')
e = combined_string.count('e')

true = t + r + u + e

l = combined_string.count('l')
o = combined_string.count('o')
v = combined_string.count('v')
e = combined_string.count('e')

love = l + o + v + e

if true and love <= 10:
    print(f"Your score is: {true}{love}, yo go together like coke and mentos.")
elif true and love >= 40 and true and love <50:
    print(f"Your score is: {true}{love}, you are alright together.")
elif true and love >= 90:
    print(f"Your score is: {true}{love}, yo go together like coke and mentos.")

else:
    print(f"Your score is: {true}{love}")















