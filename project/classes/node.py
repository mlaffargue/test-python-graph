from __future__ import annotations
import math
from typing import Set


class Node:

    def __init__(self, state: int):
        self.id: int = -1
        self.state: int = state
        self.powered: bool = False
        self.power_unit: bool = False
        self.links: Set[Node] = set()

    def get_node_position(self: Node, node_per_line: int) -> [int]:
        x = self.id % node_per_line
        y = math.floor(self.id / node_per_line)
        return [x, y]