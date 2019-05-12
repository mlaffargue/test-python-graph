from __future__ import annotations
from typing import Set


class Node:

    def __init__(self, state: int):
        self.id: int = -1
        self.state: int = state
        self.powered: bool = False
        self.power_unit: bool = False
        self.links: Set[Node] = set()
