#Cramos un nodo
class Node(): 
    def __init__(self, data): # Constructor de la clase
        self.data = data # Guardamos el dato
        self.next = None # Inicializamos el siguiente nodo como None


myNode = Node(10) # Creamos un nodo con el dato 10
print("El dato en el nodo es :", myNode.data) # Imprimimos el dato del nodo
print("EL siguiente atributo en el nodo es:", myNode.next) # Imprimimos el siguiente nodo

#Creamos una lista enlazada
class LinkedList:
    def __init__(self):
        self.Head = None

    #imprimir los elementos de una lista
    def printList(self):
        current = self.Head
        while current is not None:
            print(current.data, end=" ")
            current = current.next

myLinkedList = LinkedList()
myNode1 = Node(10)
myNode2 = Node(20)
myNode3 = Node(30)
myNode4 = Node(40)
myLinkedList.Head = myNode1
myNode1.next = myNode2
myNode2.next = myNode3
myNode3.next = myNode4

# print("Los elementos en la lista enlazada son:")
# print(myLinkedList.Head.data, end=" ")
# print(myLinkedList.Head.next.data, end=" ")
# print(myLinkedList.Head.next.next.data, end=" ")
# print(myLinkedList.Head.next.next.next.data)

print("Los elementos en la lista enlazada son:")
myLinkedList.printList()

#Imprimir los elementos de una lista enlazada