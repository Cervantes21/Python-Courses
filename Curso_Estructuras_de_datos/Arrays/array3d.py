
from array import Array

class Cube(object):
    def __init__(self, rows, cols, depth, fill_value=None):
        self.data = [[[fill_value]*depth for _ in range(cols)] for _ in range(rows)]

    def get_height(self):
        'Returns the number of rows'
        return len(self.data)

    def get_width(self):
        'Returns the number of columns'
        return len(self.data[0])

    def get_depth(self):
        return len(self.data[0][0])

    def __getitem__(self, index):
        'Supports three-dimensional indexing with[row][column][depth]'
        return self.data[index]

    def __str__(self):
        'Returns a string representation of the cube'
        result = ''

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                for depth in range(self.get_depth()):
                    result += str(self.data[row][col][depth]) + " "
                result += "\n"
        
        return str(result)

