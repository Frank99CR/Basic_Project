class Person:
    name : str

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

class Bus:
    max_passenger : int

    def __init__(self, max_passenger):
        self.max_passenger = max_passenger

    def subir_pasajeros(self, max_passenger):

        if max_passenger >= 10:
            print("No hay espacio para otro pasajero ")
        else:
            pasajero1 = Person("Alek")
            print(f"Se agrego un pasajero: ")
            print(pasajero1.print_name())


my_bus = Bus(10)

my_bus.subir_pasajeros(9)

            