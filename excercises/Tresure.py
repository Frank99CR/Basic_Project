#Fix this 
print('''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'    
''')

print("Welcome to the Treasure Island ")
print("Your mission is to find the treasure.")

right = input(print("Where do you wanna go? left or right? "))

if right == "Left":
    swim = input(print("Do you want to swim?  Yes or No"))
    if swim == "Yes":
        print("Game Over")

    else:
        print("Your getting closer to the treasure")
        door = input(print("Choose a door: Left, Center or Right"))
        if door == "Center":
            print("you found the treasure")
        else:
            print("Game over")    
else:
    print("Game Over")