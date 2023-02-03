objetivo = int(input("Choose a number: "))
epsilon = 0.001
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso
    
if abs(respuesta**2 - objetivo) >= epsilon:
    print(f"The square root of was not found: {objetivo}")
else:
    print(f"The square root of {objetivo} is {respuesta}")
        