class Node:
    data : str

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class DoubleEndedQueue:

    top : Node
    bottom : Node

    def __init__(self):   
        self.top = None
        self.bottom = None

    def push_left(self, new_node):
        current_node_left = self.bottom
        next_node = current_node_left.next
        while (next_node is not None):
            current_node_left = next_node
            next_node = current_node_left.next

        current_node_left = new_node  

    def push_right(self):
        current_node_right = self.top
        new_node = current_node_right.next
        while (new_node is not None):
            current_node_right = new_node
            new_node = current_node_right.next
        current_node_right = new_node      


    def pop_left(self):
        self.bottom = self.bottom.next

    def pop_right(self):
        self.top = self.top.next

    def print_structure():
        pass


tercer_nodo = Node("Soy el tercer nodo")
segundo_nodo = Node("Soy el segundo nodo", tercer_nodo)
primer_nodo = Node("Soy el primer nodo", segundo_nodo)

queue_doble = DoubleEndedQueue()

queue_doble.print_structure()
# queue_doble.push_right()
#queue_doble.push_left()

# queue_doble.print_structure()

# queue_doble.pop_right()
# queue_doble.pop_left()


# queue_doble.print_structure()



