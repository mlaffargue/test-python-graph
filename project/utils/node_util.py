import random

from pyx import *

from project.classes.node import Node
from project.classes.drawable_node import DrawableNode


def generate_node(c: canvas) -> Node:
    # 0 is closed, 1 is opened
    state = random.randint(0, 10)
    if state>1:
        state = 1
    return DrawableNode(state, c)


def generate_links(nodes):
    link_created = False
    while not link_created:
        # Choose 2 random nodes
        node1 = get_random_node(nodes)
        node2 = node1.get_random_linkable_node(nodes)
        link_created = node1.link_to(node2)


def get_random_node(nodes: [Node]) -> Node:
    result = -1
    while result == -1:
        result = random.randint(0, len(nodes) - 1)

    return nodes[result]


def power_node(node: Node, power_unit: bool = False):
    node.power_unit = power_unit
    if power_unit:
        node.state = 1
    node.powered = True
    for linked_node in node.links:
        if linked_node.state == 1 and not linked_node.powered:
            power_node(linked_node)
