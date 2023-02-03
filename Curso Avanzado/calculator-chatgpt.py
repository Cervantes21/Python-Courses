import os

# Clase Calculator
class Calculator():
    # constructor
    def __init__(self, a,b):
        # convertimos a a un float y lo guardamos en la propiedad del objeto
        self.a = float(a)
        # convertimos b a un float y lo guardamos en la propiedad del objeto
        self.b = float(b)

    # metodo para operar
    def operate(self, operation):
        try:
            # evaluamos la operacion y guardamos el resultado
            result = eval(f'{self.a} {operation} {self.b}')
            # imprimimos el resultado
            print(f'El resultado es: {result}')
        except:
            # si ocurre un error en la operación imprimimos un mensaje de operación inválida
            print("Operación inválida. Por favor ingresa una operación válida.")

# verificamos si el script se esta ejecutando
if __name__ == '__main__':
    while True:
        # pedimos al usuario un operador
        option = input('Escoge un operador \n 1. Sumar + \n 2. Restar - \n 3. Multiplicar *  \n 4. Dividir / \n Salir: Z \n')
        # limpiamos la pantalla
        os.system('clear')
        # verificamos si el operador es permitido
        if option in ['+', '-', '*', '/']:
            # pedimos al usuario el primer numero
            a = input('Ingresa un número: ')
            # pedimos al usuario el segundo numero
            b = input('Ingrese otro número: ')
            # creamos una instancia de Calculator
            calculator = Calculator(a,b)
            # llamamos al metodo operate con el operador seleccionado
            calculator.operate(option)
        elif option == 'z':
            print('Au revoir!!')
            break
        else:
            os.system('clear')
#AndyDollin21
# Esta calculadora fue hecha combinando mi código con CHATGPT 
