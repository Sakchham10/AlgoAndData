class CustomArray:
    def __init__(self):
        self.data = []

    def insert(self, index, value):
        self.data.insert(index, value)

    def delete(self, index):
        if 0 <= index < len(self.data):
            return self.data.pop(index)
        raise IndexError("Index out of bounds")

    def access(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        raise IndexError("Index out of bounds")

    def display(self):
        return self.data


# Example usage
array = CustomArray()
array.insert(0, 10)
array.insert(1, 20)
array.delete(0)
print(array.access(0))  # Output: 20
print(array.display())  # Output: [20]
