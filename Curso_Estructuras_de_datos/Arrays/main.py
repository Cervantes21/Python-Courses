from array3d import Cube

def cubeReto():
    cubo = Cube(3, 3, 3, fill_value="-")

    for row in range(cubo.get_height()):
        for col in range(cubo.get_width()):
            for depth in range(cubo.get_depth()):
                cubo[row][col][depth] = f'[fila {row}, Columna: {col}, Casilla {depth}]'

    print(cubo)

def run():
    cubeReto()

if __name__ == '__main__':
    run()

