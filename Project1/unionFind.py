def find(node):
    if node.parent != node:
        node.parent = find(node.parent)  # Path compression
    return node.parent


def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)

    if root1 != root2:
        if root1.rank > root2.rank:
            root2.parent = root1
        elif root1.rank < root2.rank:
            root1.parent = root2
        else:
            root2.parent = root1
            root1.rank += 1
