import os
import random as random
import math as math
import numpy as np
from bokeh.plotting import figure, output_file, show

os.system('cls')

tries = 10
puntos = 100

def estimar_pi(puntos):
    in_circle_x = []
    in_circle_y = []
    out_circle_x = []
    out_circle_y = []
    pi_array =[]

    for i in range(puntos):
        pos_x = random.uniform(-1,1)
        pos_y = random.uniform(-1,1)

        if math.sqrt(pos_x**2 + pos_y**2) <= 1:
            in_circle_x.append(pos_x)
            in_circle_y.append(pos_y)
        else:
            out_circle_x.append(pos_x)
            out_circle_y.append(pos_y)

    estimate_pi = (4 * len(in_circle_x)) / puntos
    return (estimate_pi, in_circle_x, in_circle_y, out_circle_x, out_circle_y)
    #return ()

def crear_muestra(tries):
    pi_array =[]
    for i in range(tries):
        pivalor,in_circle_x, in_circle_y, out_circle_x, out_circle_y = estimar_pi(puntos)
        pi_array.append(pivalor)
    return (pi_array, in_circle_x, in_circle_y, out_circle_x, out_circle_y)

deviation = 1       # Valor inicial para poder empezar el ciclo while
presicion = 0.1     # Precision en cifras significativas para determinar el 
                    # valor estimado de pi (CUIDADO!!!!)

iteration = 1

while deviation >= (presicion / 1.96):
    pi_array, in_circle_x, in_circle_y, out_circle_x, out_circle_y = crear_muestra(tries)
    deviation = np.std(pi_array)
    variance = np.var(pi_array) 
    mean = np.mean(pi_array)
    
    print(f'------------------       Iteracion number: {(iteration)}      ------------------')
    print(f'Standard deviation: {round(deviation,5)}, Variance : {round(variance,5)}, pi estimated: {round(mean,5)}')
    print(f'Numero de intentos {tries}, Numero de puntos {puntos}\n\n')
    #print(f)
    puntos *= 10
    tries *= 10
    iteration += 1

output_file("line.html")
plot = figure(width=600, height=600)
plot.circle(in_circle_x, in_circle_y, size=5, color="red", alpha=0.5)
plot.circle(out_circle_x, out_circle_y, size=5, color="navy", alpha=0.5)
show(plot)
