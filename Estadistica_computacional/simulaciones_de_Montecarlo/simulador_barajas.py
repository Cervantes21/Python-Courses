import random
import collections

PALOS = ['espada','corazon','rombo','trebol']

VALORES = ['as','2','3','4','5','6','7','8','9','10','jota','reina','rey']

# Crearemos nuestra función con un for loop:

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo,valor))

    return barajas

def obtener_mano(barajas, size):
    mano = random.sample(barajas, size)

    return mano

def main(hand_size, tries):
    barajas = crear_baraja()

    manos = []
    for _ in range(tries):
        mano = obtener_mano(barajas, hand_size)
        manos.append(mano)

    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 2:
                pares += 1
                break

    probabilidad_par = pares / tries
    print(f'La probabilidad de obtener un par en una mano de {hand_size} barajas es: {probabilidad_par}')

if __name__ == '__main__':
    hand_size = int(input('¿Cuántas cartas tendra la mano?: '))
    tries = int(input('¿Cuantos intentos se harán para la simulación?: '))

    main(hand_size,tries)


