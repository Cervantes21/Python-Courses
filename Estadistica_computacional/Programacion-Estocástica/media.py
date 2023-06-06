'''
# Media

- Es una medida de tendencia central.
- Comúnmente es conocida como el promedio.
- La media de una población se denota con el símbolo mu **(µ)**. La media de una muestra se denota con X.
'''

import random

def media(X):
    return sum(X) / len(X)

if __name__ == '__main__':

    X = [random.randint(1,21) for i in range(20)]
    µ = media(X)

    print(X)
    print(µ)

