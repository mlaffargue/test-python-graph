import sys
from project.classes.node import Node
from project.utils.node_util import *

sys.setrecursionlimit(10000)


if __name__ == "__main__":
    nodes_nbr = 500
    link_nbr = 300

    nodes = []

    # Generate nodes
    for i in range(nodes_nbr):
        node = generate_node()
        node.id = i
        nodes.append(node)
    for i in range(link_nbr):
        generate_links(nodes)

    # Power a random node
    power_node(get_random_node(nodes));

    for node in nodes:
        if node.powered:
            print(node.id)
