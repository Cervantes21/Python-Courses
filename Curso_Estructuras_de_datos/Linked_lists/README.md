# Nodes y singly linked list
Las estructuras linked consisten en nodos conectados a otros, los más comunes son sencillos o dobles. No se accede por índice sino por recorrido. Es decir se busca en la lista de nodos hasta encontrar un valor.

- Data: Será el valor albergado en un nodo.
- Next: Es la referencia al siguiente nodo en la lista
- Previous: Será el nodo anterior.
- Head: Hace referencia al primer nodo en la lista
- Tail: Hace referencia al último nodo.

## ¿Cómo funciona en memoria los Linked Estructures?

Estas estructuras de datos hablan de nodos/datos repartidos en memoria, diferentes a los arrays que son contiguos. Los nodos se conectan a diferentes espacios en memoria, podemos acceder a los datos saltando en memoria, siendo mucho más ágil. Los nodos nos sirven para crear otras estructuras más complejas, como Stacks, Queues, las llamadas pilas y colas. Es posible optimizar partes del código usando nodos.

- Double Linked Structure.

Estos hacen que el nodo haga referencia al siguiente nodo y al anterior, es decir nos va a permitir ir en ambas direcciones. También nos permitirá realizar “formas” y contextos circulares.

El ejemplo clave aquí será función de **ctrl+z** y **ctrl+y** Estas opciones nos permiten hacer y deshacer un proceso en Windows.

El historial del navegador también es un buen ejemplo al permitirnos navegar entre el pasado y el presente.

***Nota: Los linked list tienen una desventaja importante, si la lista crece mucho será más costoso computacionalmente recorrer toda la lista.
Es importante saber cuando usarlas y cuando no.***
