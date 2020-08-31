
from dataclasses import dataclass, asdict
from graph_util import adj_to_dot
from typing import Type, List
import math


@dataclass
class Node:
    lit: bool = False
    leaf: bool = False

    value: float = None
    rank: int = None

    max_mid: int = 0
    max_left: int = 0
    max_right: int = 0

    left: Type["Node"] = None
    right: Type["Node"] = None
    parent: Type["Node"] = None

    @property
    def pred(self):
        i = self
        while i.parent is not None and i.parent.left is i:
            i = i.parent

        i = i.parent
        if i is None or i.left is None:
            return None

        i = i.left
        while not i.leaf:
            i = i.right

        return i

    @property
    def succ(self):
        i = self
        while i.parent is not None and i.parent.right is i:
            i = i.parent

        i = i.parent
        if i is None or i.right is None:
            return None

        i = i.right
        while not i.leaf:
            i = i.left

        return i

    @property
    def dot(self):
        span = ""
        if self.rank is not None:
            span = f"({self.value - (self.rank - 1) / 2} - {self.value + (self.rank - 1) / 2})"

        color = "red" if self.leaf else "black"

        dot = f'\t {id(self)} [color={color}, pos="{self.value * 3},{math.log2(self.rank) * 3}!" label="id={self.value}\\nrank={self.rank}\\nleaf={self.leaf}\\nlit={self.lit}\\nspan={span}\\nmax={self.max_left},{self.max_mid},{self.max_right}"] \n'

        if not self.leaf:
            if self.left is not None:
                dot += f'\t {id(self)} -> {id(self.left)}\n'
                dot += self.left.dot
            if self.right is not None:
                dot += f'\t {id(self)} -> {id(self.right)}\n'
                dot += self.right.dot
        if self.leaf and not self.parent.leaf:
            if self.pred is not None:
                dot += f"\t{id(self)} -> {id(self.pred)} [color=red]\n"
            if self.succ is not None:
                dot += f"\t{id(self)} -> {id(self.succ)} [color=blue]\n"

        return dot


def prep(l, r):
    if l >= r:
        return Node(rank=1,
                    value=l,
                    leaf=True)

    mid = (l + r) // 2
    node = Node(leaf=True,
                rank=r - l + 1,
                value=(l + r) / 2,
                left=prep(l, mid),
                right=prep(mid + 1, r))

    node.left.parent = node
    node.right.parent = node
    return node


def set_lamp(node: Node, i: int, to: bool):
    if node.value == i:
        node.lit = to
        node.max_left = 1 if node.lit else 0
        node.max_mid = 1 if node.lit else 0
        node.max_right = 1 if node.lit else 0
        return
    elif node.value > i:
        set_lamp(node.left, i, to)
    else:
        set_lamp(node.right, i, to)

    both_leafs = node.left.leaf and node.right.leaf
    leaf_diff = node.left.leaf ^ node.right.leaf

    if both_leafs and not (node.left.lit ^ node.right.lit):
        assert node.left.rank == node.right.rank

        node.leaf = True
        node.lit = node.left.lit

    elif leaf_diff or (both_leafs and (node.left.lit ^ node.right.lit)):
        node.leaf = False
        node.lit = None

    if node.leaf:
        if node.lit:
            node.max_left = node.rank
            node.max_mid = node.rank
            node.max_right = node.rank
        else:
            node.max_left = 0
            node.max_mid = 0
            node.max_right = 0
    else:
        node.max_left = node.left.max_left
        node.max_right = node.right.max_right

        node.max_mid = max(node.left.max_right + node.right.max_left,
                           node.left.max_mid,
                           node.right.max_mid)


def turn_on(node: Node, i: int):
    set_lamp(node, i, True)


def turn_off(node: Node, i: int):
    set_lamp(node, i, False)


def max_darkness(node: Node):
    return max(node.max_left, node.max_mid, node.max_right)


if __name__ == "__main__":
    root = prep(0, 31)

    turn_on(root, 0)
    turn_on(root, 1)
    turn_on(root, 2)
    turn_on(root, 3)

    assert max_darkness(root) == 4

    turn_off(root, 0)
    turn_off(root, 3)

    assert max_darkness(root) == 2

    turn_on(root, 15)
    turn_on(root, 14)
    turn_on(root, 13)
    turn_on(root, 12)

    assert max_darkness(root) == 4

    turn_off(root, 14)

    assert max_darkness(root) == 2

    turn_off(root, 15)
    turn_on(root, 14)

    assert max_darkness(root) == 3

    turn_on(root, 6)
    turn_on(root, 7)
    turn_on(root, 8)
    turn_on(root, 9)

    assert max_darkness(root) == 4

    turn_on(root, 24)
    turn_on(root, 25)
    turn_on(root, 26)
    turn_on(root, 27)
    turn_on(root, 28)

    print("digraph {")
    print(root.dot)
    print("}\n\n\n\n")
