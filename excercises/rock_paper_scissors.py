import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

number_selected = input(print("What do you choose? Type 0  for rock, 1 for paper and 2 for scissors "))

num_as_integer = int(number_selected)
PC_Play = random.randint(0,2)

if num_as_integer == 0:
    print("You chose")
    print(rock)
    print("Conputer chose: ")
    if PC_Play == 0:
        print(rock)
        print("Draw")
    elif PC_Play == 1:
        print(paper)  
        print("You lose")  
    else:
        print(scissors)
        print("You win")    
    

elif num_as_integer == 1:
    print("You chose")
    print(paper)
    print("Conputer chose: ")
    if PC_Play == 0:
        print(rock)
        print("You Win")
    elif PC_Play == 1:
        print(paper)  
        print("Draw")  
    else:
        print(scissors)
        print("You lose")   

else:
    print("You chose")
    print(scissors)
    print("Conputer chose: ")
    if PC_Play == 0:
        print(rock)
        print("You lose")
    elif PC_Play == 1:
        print(paper)  
        print("You win")  
    else:
        print(scissors)
        print("Draw")   

      
    
    

