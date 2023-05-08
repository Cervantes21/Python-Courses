# Crear Nodos.

Cada nodo almacenará un valor y cada nodo tiene un puntero que llevará a otro nodo con otro valor y así obtener los datos allí almacenados.
Es muy útil al tener infromación dispersa en memoria y cuando queremos que sean consultas ágiles, es importante entender que los nodos son la base para implementaciones más elaboradas de estructuras de datos, Stacks, Qeues, Deque, Doubly, Singly List, Circular list, Graphs .

Cada estructura de datos servirá para un propósito dentro de un contexto, por ejemplo los grafos acíclicos, donde se usan para sistemas de recomendaciones al mostrar las relaciones entre objetos o representar los tipos de redes que se forman entre nodos. Para crear un nodo:

Creamos una clase Node
Referimos valores mediante argumentos de instancias.
Unimos los nodos iterando entre referencias.
Este script tiene como propósito crear nodos.

Constructor:

data= El dato del nodo.
next= está por defecto en None, porque en una serie de nodos el +ultimo te lleva a ninguna parte
