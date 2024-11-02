class Node:
    def __init__(self, value):
        self.value = value
        self.size = 0
        self.parent = self
        self.connections = {}
