from __future__ import annotations
from typing import Set


class Node:
    id: int = -1
    powered: bool = False
    links: Set[Node] = set()
    state: int

    def __init__(self, state):
        self.state = state
