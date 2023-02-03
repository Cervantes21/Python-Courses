import time

objetivo = int(input('Escoge un numero: '))
epsilon = 0.000001
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo)/2
num = 0 #numero para contar iteraciones

start = time.time()

while abs(respuesta**2 - objetivo) >= epsilon:

    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    
    respuesta = (alto + bajo)/2

    num += 1

end = time.time()

print(f'Para resolver hizo {num} iteraciones y se demoro {end - start} segundos')

print(f'La raiz cuadrada de {objetivo} es {respuesta}')

######NOTAS#####
# # numero al que se le calculará la raiz cuadrada
# objetivo = int(input('Escoge un numero: '))

# # margen de error para encontrar esa raiz cuadrada
# epsilon = 0.01

# # valor minimo para calcular largo del conjunto
# bajo = 0.0

# # valor maximo para calcular largo de conjunto. Función max() >> elegirá el valor máximo de los parámetros que le demos; colocamos 1.0 como valor mínimo aceptado (así nos cubrimos de que, por ejemplo, el usuario coloque un valor negativo), y objetivo (valor que nos dará el usuario)
# alto = max(1.0, objetivo)

# # aqui generamos el valor medio de nuestro conjunto, a lo cual se puede genera el condicional (if) para elegir la mitad menor o la mitad mayor.
# respuesta = (alto + bajo) / 2

# # para entender esto, lo más fácil es imaginar que el while saltará de un grupo de mitades a otro, dependiendo de la situación, hasta que el grupo se divida lo suficiente como para dar con el objetivo.

# # el while comienza diciendo que, hasta que la respuesta de con el resultado (con un margen de error de 0.01, es decir epsilon), se hará la iteración del paso 2 de este algoritmo. 
# while abs(respuesta**2 - objetivo) >= epsilon:
#     # si respuesta**2 no es mayor que objetivo, quiere decir que respuesta debe ser mayor (de respuesta para abajo, no nos sirve; nos sirve el rango de respuesta para arriba). 
#     # RECORDAR: respuesta es el valor medio del conjunto que estamos analizando (mirar más arriba)
#     if respuesta**2 < objetivo:
#         # como sabemos que de respuesta para abajo no tenemos un valor que nos sirva, actualizamos el piso (bajo) de nuestro conjunto a el valor actual de respuesta.
#         bajo = respuesta
#     # si respuesta**2 es mayor que objetivo, quiere decir que respuesta debe ser menor (de respuesta para arriba, no nos sirve; nos sirve el rango de respuesta para abajo)
#     else:
#         # como sabemos que respuesta para arriba no tenemos un valor que nos sirva, actualizamos el techo (alto) de nuestro conjunto a el valor actual de respuesta
#         alto = respuesta

#     # Saliendo del else, ejecutamos el código para que respuesta (punto medio de nuestro conjunto) se actualice al nuevo conjunto.
#     respuesta = (alto + bajo) / 2

# ##################################
# # Repitiendo este loop, llegará un punto en el que el conjunto sea muy pequeño, y hallaremos la raiz cuadrada.
# # Los loops necesarios serán mucho menos que si usamos busqueda exhaustiva o aproximacion

# print(f'La raiz cuadrada de {objetivo} es {respuesta}')