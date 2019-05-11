import random

from project.classes.node import Node


def generate_node():
    # 0 is closed, 1 is opened
    state = random.randint(0, 10)
    if state>1:
        state = 1
    return Node(state)


def create_link(node1: Node, node2: Node, node_per_line):
    # only connect nodes that are side by side
    position1 = node1.get_node_position(node_per_line)
    position2 = node2.get_node_position(node_per_line)

    if abs(position1[0] - position2[0]) == 1 and position1[1] == position2[1] or \
            abs(position1[1] - position2[1]) == 1 and position1[0] == position2[0]:
        if node2 not in node1.links:
            node1.links.add(node2)
            node2.links.add(node1)
        return True
    return False


def generate_links(nodes, node_per_line):
    link_created = False
    while not link_created:
        # Choose 2 random nodes
        node1 = get_random_node(nodes)
        node2 = get_random_node(nodes, node1.id)
        link_created = create_link(node1, node2, node_per_line)


def get_random_node(nodes: [Node], avoid=-1):
    result = -1
    while result == -1:
        result = random.randint(0, len(nodes) - 1)
        if result == avoid:
            result = -1
    return nodes[result]


def power_node(node: Node, power_unit: bool = False):
    node.power_unit = power_unit
    if power_unit:
        node.state = 1
    node.powered = True
    for linked_node in node.links:
        if linked_node.state == 1 and not linked_node.powered:
            power_node(linked_node)
