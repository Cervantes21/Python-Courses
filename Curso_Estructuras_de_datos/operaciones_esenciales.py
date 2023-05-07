'''
Crea espacios hacia la derecha si el número lower es menor que el número upper, cuando son diferentes, en cada llamada el número lower base aumenta en 1 y la margen en 4 espacios.

El propósito de este  snipet  de código es ejemplificar qué tipo de conceptos (funciones, condicionales, recursividad) veremos en las estructuras de datos como métodos de clase. Si no entiendes la función no te rindas :), repasa y regresa.

'''


def pyramid_sum(lower, upper, margin =0):
	blanks = " " * margin
	print(blanks, lower, upper)
	if lower > upper:
		print(blanks, 0)
		return 0
	else:
		# Llamada recursiva
		result = lower+ pyramid_sum(lower + 1, upper, margin +4)
		print(blanks, result)
		return result

  
 
pyramid_sum(1,10)
