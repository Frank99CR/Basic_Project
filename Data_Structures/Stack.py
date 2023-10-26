class Node:
    data : str

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    
    top : Node

    def __init__(self):
        self.top = None

    def push(self, new_node):  
        new_node.next = self.top
        self.top = new_node
        

    def pop(self): 
        self.top = self.top.next 

    def print_stack(self):
     current_node = self.top
     while (current_node is not None):
         print(current_node.data)
         current_node = current_node.next
     



        
tercer_nodo = Node("Nodo 3")
segundo_nodo = Node("Nodo 2", tercer_nodo)
primer_nodo = Node("Nodo 1", segundo_nodo)

my_stack = Stack()
my_stack.push(primer_nodo)
my_stack.push(segundo_nodo)
my_stack.push(tercer_nodo)
my_stack.print_stack()
print("Eliminando")
my_stack.pop()
my_stack.print_stack()
print("Eliminando")
my_stack.pop()
my_stack.print_stack()
# print("Eliminando")
# my_stack.pop()
# my_stack.print_stack()



