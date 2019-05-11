import random

from project.classes.node import Node


def generate_node():
    # 0 is closed, 1 is opened
    return Node(random.randint(0, 1))


def create_link(node1, node2):
    if node2 not in node1.links:
        node1.links.add(node2)
        node2.links.add(node1)
        return True
    return False


def generate_links(nodes):
    link_created = False
    while not link_created:
        # Choose 2 random nodes
        node1 = get_random_node(nodes)
        node2 = get_random_node(nodes, node1.id)
        link_created = create_link(node1, node2)


def get_random_node(nodes: [Node], avoid=-1):
    result = -1
    while result == -1:
        result = random.randint(0, len(nodes) - 1)
        if result == avoid:
            result = -1
    print(nodes[result], " ", result)
    return nodes[result]


def power_node(node: Node):
    node.powered = True
    for linked_node in node.links:
        if linked_node.state == 1 and not linked_node.powered:
            power_node(linked_node)
