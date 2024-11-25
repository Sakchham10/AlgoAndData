class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        raise IndexError("Peek from empty stack")

    def is_empty(self):
        return len(self.data) == 0

    def display(self):
        return self.data


# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.pop()
print(stack.peek())  # Output: 10
print(stack.display())  # Output: [10]
