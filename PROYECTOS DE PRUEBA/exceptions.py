
def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista
   

lista = list(range(10))
divisor = 2

print(divide_elementos_de_lista(lista, divisor))