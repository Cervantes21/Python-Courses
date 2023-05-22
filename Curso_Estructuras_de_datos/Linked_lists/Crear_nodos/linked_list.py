
# Crear Singly linked list:
from nodos import Node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0 

    def add_to_start(self, data):
        """Inserta un nodo al inicio."""
        self.head = Node(data, self.head)
        print(f"Nodo {self.head.data} añadido a la cabezera.")
        self.size += 1

    def append(self, data):
        """Añade un nodo nuevo al final."""
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            probe = self.head
            while probe.next:
                probe = probe.next
            probe.next = node
        print(f"Nodo {node.data} añadido a la cola.")
        self.size += 1

    def insert(self, data, index):
        """Inserta un nodo segun indice."""
        if index > self.count_nodes():
            print("El indice supera la cantidad de nodos")
        else:
            if self.head is None or index <= 0:
                self.head = Node(data, self.head)
            else:
                probe = self.head
                index -= 1
                while index > 1 and probe.next != None:
                    probe = probe.next
                    index -= 1
                probe.next = Node(data, probe.next)
            print(f"Nodo {data} añadido.")
            self.size += 1

    def replace(self, data, new_data):
        """Reemplaza un nodo por uno nuevo."""
        probe = self.head
        while probe != None and data != probe.data:
            probe = probe.next
        if probe != None:
            probe.data = new_data
            print(f"El nodo {data} ha sido reemplazado por {new_data}")
        else:
            print(f"The target item {data} is not in the linked list")

    def delete(self, index):
        """Elimina nodo en posición dada."""
        if index > self.count_nodes():
            print("El indice supera la cantidad de nodos")
        else:
            if self.head is None:
                print("No hay nodos que eliminar.")
            elif self.head.next is None:
                print(f"Nodo: {self.head.data} eliminado.")
                self.head = None
                self.size -= 1
            else:
                probe = self.head
                index -= 1
                while index > 1 and probe.next.next != None:
                    probe = probe.next
                    index -= 1
                removed_item = probe.next.data
                probe.next = probe.next.next
                print(f"Nodo:{removed_item} eliminado.")
                self.size -= 1

    def pop(self):
        """Elimina ultimo nodo."""
        data = self.head.data
        if self.head.next is None:
            self.head = None
        else:
            probe = self.head
            while probe.next.next != None:
                probe = probe.next
            data = probe.next.data
            probe.next = None
        self.size -= 1
        print(f"Ultimo nodo {data} eliminado.")

    def search(self, data):
        """Busca nodo especificado."""
        probe = self.head
        while probe != None and data != probe.data:
            probe = probe.next
        if probe != None:
            print(f"El nodo {data} ha sido encontrado.")
            return probe
        else:
            print(f"El nodo {data} no se encuentra en el grafo.")

    def count_nodes(self):
        """Imprime cantidad de nodos."""
        return self.size

    def print(self):
        """Imprime cada nodo."""
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next
    
    def clear(self):
        self.head = None
        self.size = 0
    
    def iter(self):
        """Iteracion en cada nodo."""
        current = self.tail
        
        while current:
            val = current.data
            current = current.next
            yield val
    
        
if __name__ == '__main__':
    # Reto
    array = [2, 4, 6]
    datos = SinglyLinkedList()

    for i in array:
        datos.append(i)
    current = datos.tail
    
    while current:
        print(current.data)
        current = current.next
        