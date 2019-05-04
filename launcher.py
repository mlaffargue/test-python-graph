import random

class Node:
    def __init__(self, state):
        self.state = state
        self.id = -1
        self.links = set()
        self.powered = False

def generate_node():
    # 0 is closed, 1 is opened
    node = Node(random.randint(0, 1))
    return node


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


if __name__ == "__main__":
    nodes_nbr = 20000
    link_nbr = 10000

    nodes = []

    # Generate nodes
    for i in range(nodes_nbr):
        node = generate_node()
        node.id = i
        nodes.append(node)
    for i in range(link_nbr):
        generate_links(nodes)

    for i in range(nodes_nbr):
        print(i, "-->", nodes )