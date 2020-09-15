from random import Random
from dataclasses import dataclass, field
from typing import List


@dataclass
class Node:
    level: int = 8
    forward: List["Node"] = field(init=False, repr=False)
    value: int = None

    def __post_init__(self):
        self.forward = [None] * self.level


@dataclass
class SkipList:
    sentinel: Node = field(init=False)
    max_level: int = 4

    def __post_init__(self):
        self.sentinel = Node(level=self.max_level)

    def add(self, value):
        random = Random(42 ** value)

        new = Node(value=value, level=random.randint(1, self.max_level))
        update = [None] * (self.max_level + 1)

        node = self.sentinel
        for lvl in range(self.max_level - 1, -1, -1):
            while node.forward[lvl] is not None and node.forward[lvl].value < new.value:
                node = node.forward[lvl]
            update[lvl] = node

        for lvl in range(new.level):
            new.forward[lvl] = update[lvl].forward[lvl]
            update[lvl].forward[lvl] = new

    def get(self, value):
        node = self.sentinel
        for lvl in range(self.max_level - 1, -1, -1):
            while node.forward[lvl] is not None and node.forward[lvl].value < value:
                node = node.forward[lvl]

        if node is None or node.forward[0] is None:
            return None

        node = node.forward[0]

        if node.value == value:
            return node.value

        return None


if __name__ == "__main__":
    li = SkipList()
    li.add(32)
    li.add(10)
    li.add(16)
    li.add(8)
    li.add(12)
    li.add(18)

    node = li.sentinel
    print(f"l | ", end="")
    while node is not None:
        print(node.level, end=", ")
        node = node.forward[0]
    print()

    for i in range(li.max_level):
        node = li.sentinel
        print(f"{i} | ", end="")
        while node is not None:
            print(node.value, end=", ")
            node = node.forward[i]
        print()

    print(li.get(10))

    assert li.get(32) == 32
    assert li.get(10) == 10
    assert li.get(16) == 16
    assert li.get(8) == 8
    assert li.get(12) == 12
    assert li.get(1832) is None
    assert li.get(10) == 10
    assert li.get(16) == 16
    assert li.get(8) == 8
    assert li.get(12) == 12
    assert li.get(18) == 18

    print()
