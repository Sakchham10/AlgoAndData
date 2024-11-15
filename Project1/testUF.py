from node import Node
from unionFind import find, union

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

union(node1, node2)
union(node2, node4)
find(node4)
