'''
# VARIANZA
- La varianza mide que tan propagados se encuentran un conjunto de valores aleatorios de su media.
- Mientras que la media nos da una idea de dónde se encuentran los valores, la varianza nos dice que tan dispersos se encuentran los valores.
- La varianza siempre debe entenderse con respecto a la media.
'''

'''
# Desviación estándar:
- La desviación estándar es la raíz cuadrada de la varianza.
- Nos permite entender, también, la propagación y se debe entender siempre relacionado a la media.
- La ventaja sobre la varianza es que la desviación estándar está en las mismas unidades que la media.
'''

import random
import math
from media import media

def varianza(X):
    mu = media(X)

    acumulador = 0
    for x in X:
        acumulador += (x - mu)**2

    return acumulador / len(X)

def desviacion_estandar(X):
    return math.sqrt(varianza(X))

if __name__ == '__main__':

    X = [random.randint(1,21) for i in range(20)]
    µ = media(X)
    var = varianza(X)
    sigma = desviacion_estandar(X)

    print(f'Arreglo X: {X}')
    print(f'Media = {µ}')
    print(f'Varianza = {var}')
    print(f'Desviacion estandar = {sigma}')


