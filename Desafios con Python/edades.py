import random

# Crear un array vacío
edades = []

# Agregar 100 edades aleatorias al array
for i in range(100):
    try:
        edad = random.randint(17, 55)
        if edad < 18:
            raise ValueError("La edad es menor a 18 años")
        edades.append(edad)
    except ValueError as e:
        print(f"Error: {e}")

# Imprimir el array de edades
print(edades)

