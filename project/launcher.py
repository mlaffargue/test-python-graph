import sys
from pyx import *
from project.utils.node_util import *

sys.setrecursionlimit(10000)


if __name__ == "__main__":
    c = canvas.canvas()

    nodes_nbr = 900
    max_link_nbr = 800
    node_per_line = 30
    power_unit_nbr = 10

    nodes = []
    DrawableNode.node_per_line = node_per_line

    # Generate nodes
    for i in range(nodes_nbr):
        node = generate_node(c)
        node.id = i
        nodes.append(node)
    for i in range(max_link_nbr):
        generate_links(nodes)

    # Power a random node
    for i in range(power_unit_nbr):
        power_node(get_random_node(nodes), True)

    for node in nodes:
        node.draw();

    c.writePDFfile("result")
