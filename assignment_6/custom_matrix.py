class CustomMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def insert(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            raise IndexError("Index out of bounds")

    def delete(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = 0
        else:
            raise IndexError("Index out of bounds")

    def access(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        raise IndexError("Index out of bounds")

    def display(self):
        return self.data


# Example usage
matrix = CustomMatrix(3, 3)
matrix.insert(1, 1, 5)
matrix.delete(1, 1)
print(matrix.access(1, 1))  # Output: 0
print(matrix.display())  # Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
