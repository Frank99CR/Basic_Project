class Node:
    data : str

    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left

class BinaryTree:
    root : Node  

    def __init__(self, root=None): 
        self.root = root  
        

    def print_structure(self, node):
         if node is not None:
            print(node.data)
            self.print_structure(node.right)
            self.print_structure(node.left)
            
            
node_hijo_derecha1 = Node("Soy el hijo 1 de la derecha")    
node_hijo_derecha2 = Node("Soy el hijo 2 de la derecha")
node_hijo_izquierda1 = Node("Soy el hijo 1 de la izquierda")    
node_hijo_izquierda2 = Node("Soy el hijo 2 de la izquierda")
Nodo_Derecha = Node("Soy el Nodo de la derecha", node_hijo_derecha1, node_hijo_derecha2)
Nodo_Izquierda = Node("Soy el Nodo de la Izquierda", node_hijo_izquierda1, node_hijo_izquierda2)
nodo_raiz = Node("Soy el Root", Nodo_Derecha, Nodo_Izquierda)

BinaryT = BinaryTree()
BinaryT.print_structure(nodo_raiz)