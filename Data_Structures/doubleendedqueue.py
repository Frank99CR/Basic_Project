class Node:
    data : str

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class DoubleEndedQueue:

    top : Node
    bottom : Node

    def __init__(self, top =None, bottom=None):   
        self.top = top
        self.bottom = bottom

    def push_left(self, new_node):
        if self.bottom == None:
            self.bottom = new_node
        new_node.next = self.top
        self.top = new_node

    def push_right(self, new_node):
        if self.top == None:
          self.top = new_node
        if self.bottom:
         self.bottom.next = new_node
        self.bottom = new_node

       
        
        
    def pop_left(self):
        self.top = self.top.next 

    def pop_right(self):
         
         current_node = self.bottom
         next_node = current_node.next
         while (current_node.next is not self.bottom):
          current_node.next = None
          self.bottom =  current_node

 
    def print_structure(self):
        current_node = self.top
        while(current_node is not None):
            print(current_node.data)
            current_node = current_node.next
          

cuarto_nodo = Node("Soy el cuarto nodo")
tercer_nodo = Node("Soy el tercer nodo")
segundo_nodo = Node("Soy el segundo nodo")
primer_nodo = Node("Soy el primer nodo")

queue_doble = DoubleEndedQueue()

#queue_doble.print_structure()

queue_doble.push_left(segundo_nodo)
queue_doble.push_left(primer_nodo)
#queue_doble.print_structure()
queue_doble.push_right(tercer_nodo)
queue_doble.push_right(cuarto_nodo)

# queue_doble.pop_right()
#queue_doble.pop_left()


#queue_doble.print_structure()
print("Pop Right")
queue_doble.pop_right()
queue_doble.print_structure()



