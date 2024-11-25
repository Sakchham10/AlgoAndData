import random
import time

from graph import Graph


def create_test_graph(x, y):
    start_time = time.time()
    # Initialize the graph
    test_graph = Graph()

    # Add x nodes
    for node in range(1, x + 1):
        test_graph.add_node(node)

    # Add y edges
    added_edges = 0
    while added_edges < y:
        # Randomly pick two distinct nodes
        from_node = random.randint(1, x)
        to_node = random.randint(1, x)
        while to_node == from_node:  # Ensure no self-loop
            to_node = random.randint(1, x)

        # Assign a random weight for the edge
        weight = random.randint(1, 10)

        # Add the edge
        test_graph.add_edge(from_node, to_node, weight)
        added_edges += 1
    for r in range(1, 10):
        from_node = random.randint(1, r)
        to_node = random.randint(1, r)
        test_graph.find_node(test_graph.nodes[from_node], test_graph.nodes[to_node])
    end_time = time.time()
    print(f"For graph with {x} nodes and {y} edges")
    print(f"Time taken is {end_time - start_time} seconds")
    return test_graph


create_test_graph(100, 50)
create_test_graph(1000, 500)
create_test_graph(10000, 5000)
