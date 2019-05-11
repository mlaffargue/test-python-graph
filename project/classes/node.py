class Node:
    id: int = -1
    powered: bool = False
    links = set()      # type: set[Node]

    def __init__(self, state):
        self.state = state      # type: int
