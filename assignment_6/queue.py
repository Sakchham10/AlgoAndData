class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.data.pop(0)
        raise IndexError("Dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.data[0]
        raise IndexError("Peek from empty queue")

    def is_empty(self):
        return len(self.data) == 0

    def display(self):
        return self.data


# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.dequeue()
print(queue.peek())  # Output: 20
print(queue.display())  # Output: [20]
