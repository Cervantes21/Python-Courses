import random

# ------------------------------------ #

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []
    for _ in range(numero_de_tiros):
# Usando choice:
        tiro = random.choice([1,2,3,4,5,6]) 
# Usando randint:
      #  tiro = random.randint(1,7) # Creamos las caras del dado.
        secuencia_de_tiros.append(tiro)
        # Actualizamos nuestra lista.
        
    return secuencia_de_tiros

# ------------------------------------#

def main(numero_de_tiros,numero_de_intentos):
    tiros=[]
    # Agregamos una lista vacia que contendra nuestros resultados.
    for _ in range(numero_de_intentos):
        secuencia = tirar_dado(numero_de_tiros)
        # Una variable de nuestra secuencia de tiros.
        tiros.append(secuencia)
        # Actualizamos nuestra lista

# Probabilidad:
    tiros_con_1 = 0
    # Comenzamos nuestra variable de conteo
    for tiro in tiros:
    # por cada tiro en tiros que:
        if 1 in tiro:
    # si en tiro hay 1:
            tiros_con_1 += 1
            # Sumaremos a nuestro contador cada que regriste uno de nuestra tirada.
    probabilidad_tiros_con_1 = tiros_con_1 / numero_de_intentos
    # Aquí la formula esta contando los tiros que tengan 1, y lo divide entre el número de intnetos.

# La predicción:
# P(1) = 1/6 | 1-P(1)= 1-1/6=5/6=0.83
# Por cada 10 intentos sería: 5/6**10≈0.1615
    print(f'La probabilidad de obtener 1 por lo menos en {numero_de_tiros} tiros es igual a {probabilidad_tiros_con_1}')


# ------------------------------------ #

if __name__ == '__main__':

    numero_de_tiros = int(input('¿Cuántas tiradas hará el dado? '))
    numero_de_intentos = int(input('¿Cuántas veces quieres correr la simulación? '))
    # Cada que nuestra población tienda a infinito, nuestros datos tendrán menor sesgo.
    
    main(numero_de_tiros, numero_de_intentos)
    # Llamámos a nuestra función
