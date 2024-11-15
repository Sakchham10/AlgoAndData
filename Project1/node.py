class Node:
    def __init__(self, value):
        self.value = value
        self.size = 0
        self.parent = self
        self.connections = {}

    def add_edge(self, node, weight):
        if node not in self.connections:
            self.connections[node] = 0
        self.connections[node] = weight
