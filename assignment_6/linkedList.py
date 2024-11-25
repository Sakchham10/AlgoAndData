class Node:
    def __init__(self, value):
        self.value = value
        self.next_val = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_val:
                current = current.next_val
            current.next_val = new_node

    def delete(self, value):
        if not self.head:
            raise ValueError("List is empty")
        if self.head.value == value:
            self.head = self.head.next_val
            return
        current = self.head
        while current.next_val and current.next_val.value != value:
            current = current.next_val
        if current.next_val:
            current.next_val = current.next_val.next_val
        else:
            raise ValueError(f"Value {value} not found in list")

    def traverse(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next_val
        return result


# Example usage
linked_list = SinglyLinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.delete(10)
print(linked_list.traverse())  # Output: [20]
