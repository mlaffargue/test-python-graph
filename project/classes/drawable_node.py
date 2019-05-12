from __future__ import annotations

import math
import random

from pyx import *

from project.classes.node import Node


class DrawableNode(Node):
    node_per_line: int

    def __init__(self, state: int, c: canvas):
        Node.__init__(self, state)
        self.c: canvas = c

    def link_to(self: Node, node: Node) -> bool:
        # only connect nodes that are side by side
        position1 = self.get_node_position()
        position2 = node.get_node_position()

        if abs(position1[0] - position2[0]) == 1 and position1[1] == position2[1] or \
                abs(position1[1] - position2[1]) == 1 and position1[0] == position2[0]:
            if node not in self.links:
                self.links.add(node)
                node.links.add(self)
            return True
        return False

    def get_random_linkable_node(self: Node, nodes: [Node]) -> Node:
        result = random.randint(1, 4)
        position = self.get_node_position()
        positions = {
            1: [position[0]-1, position[1]],  # LEFT
            2: [position[0]+1, position[1]],  # RIGHT
            3: [position[0], position[1]-1],  # TOP
            4: [position[0], position[1]+1]  # BOTTOM
        }

        # Corner cases
        result = self.handle_corners(nodes, position, result)
        # Border cases
        result = self.handle_borders(nodes, position, result)
        idx = positions[result][1] * DrawableNode.node_per_line + positions[result][0]

        return nodes[idx]

    def handle_borders(self: Node, nodes: [Node], position: [int], result: int) -> int:
        if position[0] == 0 and result == 1:
            result = random.randint(2, 4)
        if position[0] == DrawableNode.node_per_line - 1 and result == 2:
            while result == 2:
                result = random.randint(1, 4)
        if position[1] == 0 and result == 3:
            while result == 3:
                result = random.randint(1, 4)
        if position[1] == len(nodes) / DrawableNode.node_per_line - 1 and result == 4:
            while result == 4:
                result = random.randint(1, 4)
        return result

    def handle_corners(self: Node, nodes: [Node], position: [int], result: int) -> int:
        # Top/Left
        if position[0] == 0 and position[1] == 0 and (result == 1 or result == 3):
            while result == 1 or result == 3:
                result = random.randint(1, 4)
        # Top/Right
        if position[0] == DrawableNode.node_per_line - 1 and position[1] == 0 and (result == 2 or result == 3):
            while result == 2 or result == 3:
                result = random.randint(1, 4)
        # Bottom/Left
        if position[0] == 0 and position[1] == len(nodes) / DrawableNode.node_per_line - 1 and (
                result == 1 or result == 4):
            while result == 1 or result == 4:
                result = random.randint(1, 4)
        # Bottom/Right
        if position[0] == DrawableNode.node_per_line - 1 and position[1] == len(
                nodes) / DrawableNode.node_per_line - 1 and (result == 2 or result == 4):
            while result == 2 or result == 4:
                result = random.randint(1, 4)
        return result

    def get_node_position(self: Node) -> [int]:
        x = self.id % DrawableNode.node_per_line
        y = math.floor(self.id / DrawableNode.node_per_line)
        return [x, y]

    def draw(self: DrawableNode):
        position = self.get_node_position()
        if self.power_unit:
            self.c.stroke(path.circle(position[0], position[1], 0.4),
                          [style.linewidth.Thick, deco.filled([color.rgb.blue])])

        if self.powered:
            self.c.stroke(path.circle(position[0], position[1], 0.3), [deco.filled([color.rgb.green])])
        else:
            self.c.stroke(path.circle(position[0], position[1], 0.3))

        if self.state == 0:
            self.c.stroke(path.circle(position[0], position[1], 0.3), [deco.filled([color.rgb.red])])
            size = 0.1
            self.c.stroke(path.line(position[0]-size, position[1]-size, position[0]+size, position[1]+size))
            self.c.stroke(path.line(position[0]-size, position[1]+size, position[0]+size, position[1]-size))

        # Draw links
        for linked_node in self.links:
            position_linked = linked_node.get_node_position()
            self.c.stroke(path.line(position[0], position[1], position_linked[0], position_linked[1]))