class Person:
    name : str

    def __init__(self, name):
        self.name = name


class Bus:
    max_passenger : int
    passenger_on_us : list
    
    

    def __init__(self, max_passenger, passenger_on_bus):
        self.max_passenger = max_passenger
        self.passenger_on_bus = passenger_on_bus
        

    def subir_pasajeros(self, new_passenger):

        if len(self.passenger_on_bus) >= self.max_passenger:
            print("No hay espacio para otro pasajero ")
           
        else:
            self.passenger_on_bus.append(new_passenger)
            print(f"Nuevo pasejero en el bus. ")
            


my_passenger1 = Person ("Francisco")
my_passenger2 = Person ("Valeria")
my_passenger3 = Person ("Alek")
my_passenger4 = Person ("Olde")
my_passenger5 = Person ("Sandi")

my_passenger6 = Person("Susana")
my_passenger7 = Person("Maria Solano")
my_passenger8 = Person("Marlon")

list_of_passengers = [my_passenger1, my_passenger2, my_passenger3, my_passenger4, my_passenger5]



my_bus = Bus(6, list_of_passengers)

my_bus.subir_pasajeros(my_passenger7)
my_bus.subir_pasajeros(my_passenger6)
my_bus.subir_pasajeros(my_passenger8)