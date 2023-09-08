print("Welcome to Pizza Python Deliveries!")
pizza = input(print("What size pizza do you want? S, M or L"))
Pepperoni = input(print("Do you want pepperoni? Y or N"))
Chesse = input(print("Do you want extra cheese? Y or N" ))

small_pizza = 15
medium_pizza = 20
large_pizza = 25

if pizza == "S":
    small_pizza
    if Pepperoni == "Y":
        small_pizza += 2
        if Chesse == "Y":
            small_pizza += 1
            print(f"Your final bill is: ${small_pizza}")
        else:
            print(f"Your final bill is: ${small_pizza}")    
    else:
        print(f"Your bills is: $ {small_pizza}")   
elif pizza == "M":
    medium_pizza
    if Pepperoni == "Y":
        medium_pizza += 3
        if Chesse == "Y":
            medium_pizza += 1
            print(f"Your final bill is: ${medium_pizza}")
        else:
            print(f"Your final bill is: ${medium_pizza}")    
    else:
        print(f"Your final bill is: ${medium_pizza}")    
elif pizza == "L": 
    large_pizza
    if Pepperoni == "Y":
        large_pizza += 3
        if Chesse == "Y":
            large_pizza += 1
            print(f"Your final bill is: ${large_pizza}")
        else:
            print(f"Your final bill is: ${large_pizza}")    
    else:
        print(f"Your final bill is: ${large_pizza}")
else:
    print("Invalid data!")       

 