class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __str__(self):
        result = ''
        for i in range(self.rows):
            for j in range(self.cols):
                result += str(self.matrix[i][j]) + ' '
            result += '\n'
        return result

    def __add__(self, other):
        result = [[0 for j in range(self.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(result)


m1 = Matrix([[1, 2, 3], [4, 5, 6]])
m2 = Matrix([[6, 5, 4], [3, 2, 1]])
m3 = m1 + m2
print(m3)