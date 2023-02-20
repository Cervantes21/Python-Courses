import sys
# def fibonacci_recursivo(n):
#     if n == 0 or n == 1:
#         return 1

#     return fibonacci_recursivo(n-1) + fibonacci_recursivo(n - 2)


def fibonacci_dinamico(n, memo = {}): # Agregamos otro parámetro, en este caso será memo un diccionario que contendra nuestros resutaldos.
    if n == 0 or n == 1:
        return 1
    # Le decimos que en caso que el número sea 0, o 1 regresará 1.
    try:
        return memo[n]
    # Si tenemos el resultado lo devolverá
    except KeyError:
    # De lo contrario que no tengamos el valor lo creará.
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        # Nuestra función fibonacci estará almacenada en una variable llamada resultado.
        # Con ella estamos llamando a nuestra función de n-1 junto con la memoria, más la función de fibonaccio de n-2 junto con la memoria.
        memo[n] = resultado
        # Actualizamos el la memoria con el resultado.
        return resultado
    
if __name__ == '__main__':
# Entrypoint

    sys.setrecursionlimit(10002)
    # Aquí estamos elimando el problema de la recursión limitada. 
    # Esto quiere decir que nos da cierto espacio para mostrar más digitos.
    n = int(input('Escoge un número: '))
    # Le pedimos al usuario que nos de un valor a calcular.
    resultado = fibonacci_dinamico(n)
    # Guardamos la llamada de nuestra función
    print(resultado)
    # Mostramos en pantalla el resultado
    
