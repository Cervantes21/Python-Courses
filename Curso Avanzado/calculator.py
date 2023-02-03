import os

class Calculator():
    a = 0
    b = 0

    def __init__(self, a,b):
        self.a = float(a)
        self.b = float(b)

    def sumar(self):
        suma = self.a + self.b
        print (f'Tu resultado es: {suma}')

    def restar(self):
        resta = self.a - self.b
        print (f'Tu resultado es: {resta}')
        
    def multiplicar(self):
        multiplication = self.a * self.b
        print (f'Tu resultado es: {multiplication}')

    def dividir(self):
        while True:
            try:
                division = self.a / self.b
                print (f'Tu resultado es: {division}')
            except ZeroDivisionError:
                os.system('clear')
                print ('No se puede dividir entre 0')
                break

if __name__ == '__main__':
    pass
while True:
    option = input('Escoge un operador \n 1. Sumar + \n 2. Restar - \n 3. Multiplicar *  \n 4. Dividir / \n Salir: Z \n')
    os.system('clear')
    if option == '+':
        a = input('Ingresa un número: ')
        b = input('Ingrese otro número: ')
        calculator = Calculator(a,b)
        calculator.sumar()

    elif option == '-':
        a = input('Ingresa un número: ')
        b = input('Ingrese otro número: ')
        calculator = Calculator(a,b)
        calculator.restar()

    elif option == '*':
        a = input('Ingresa un número: ')
        b = input('Ingrese otro número: ')
        calculator = Calculator(a,b)
        calculator.multiplicar()

    elif option == '/':
        a = input('Ingresa un número: ')
        b = input('Ingrese otro número: ')
        calculator = Calculator(a,b)
        calculator.dividir()

    elif option == 'z':
        print('Au revoir!!')
        break

    else:
        os.system('clear')
        print ('Opción incorrecta \nutiliza un símbolo de operador como \n+, -, *, /\n')
        continue
