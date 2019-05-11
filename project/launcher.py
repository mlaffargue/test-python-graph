import sys
from pyx import *
from project.utils.node_util import *

sys.setrecursionlimit(10000)


if __name__ == "__main__":
    c = canvas.canvas()

    nodes_nbr = 3600
    link_nbr = 3000
    node_per_line = 60
    power_unit_nbr = 20

    nodes = []

    # Generate nodes
    for i in range(nodes_nbr):
        node = generate_node()
        node.id = i
        nodes.append(node)
    for i in range(link_nbr):
        generate_links(nodes, node_per_line)

    # Power a random node
    for i in range(power_unit_nbr):
        power_node(get_random_node(nodes), True)

    for node in nodes:
        position = node.get_node_position(node_per_line)
        if node.power_unit:
            c.stroke(path.circle(position[0], position[1], 0.4), [style.linewidth.Thick, deco.filled([color.rgb.green])])
        if node.powered:
            c.stroke(path.circle(position[0], position[1], 0.3), [deco.filled([color.rgb.green])])
        else:
            c.stroke(path.circle(position[0], position[1], 0.3))

        if node.state == 0:
            size = 0.1
            c.stroke(path.line(position[0]-size, position[1]-size, position[0]+size, position[1]+size))
            c.stroke(path.line(position[0]-size, position[1]+size, position[0]+size, position[1]-size))

        # Draw links
        for linked_node in node.links:
            position_linked = linked_node.get_node_position(node_per_line)
            c.stroke(path.line(position[0], position[1], position_linked[0], position_linked[1]))

    c.writePDFfile("result")
    