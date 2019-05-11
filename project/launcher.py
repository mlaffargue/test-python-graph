import random
import sys
from pythongraphpowering.node import node

sys.setrecursionlimit(10000)

def generate_node():
    # 0 is closed, 1 is opened
    return Node(random.randint(0, 1))


def create_link(node1, node2):
    if node2 not in node1.links:
        node1.links.add(node2)
        node2.links.add(node1)
        return True
    return False


def generate_links(nodes_):
    link_created = False
    while not link_created:
        # Choose 2 random nodes
        node1 = get_random_node(nodes_)
        node2 = get_random_node(nodes_, node1.id)
        link_created = create_link(node1, node2)


def get_random_node(nodes_, avoid = -1):
    result = -1
    while result == -1:
        result = random.randint(0, len(nodes_) - 1)
        if result == avoid:
            result = -1
    return nodes_[result]


def power_node(node_: Node):
    node_.powered = True
    for linked_node in node_.links:
        if linked_node.state == 1 and not linked_node.powered:
            power_node(linked_node)


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
    powered_node = get_random_node(nodes)
    power_node(powered_node);

    for node in nodes:
        if node.powered:
            print(node.id)