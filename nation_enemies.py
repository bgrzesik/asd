import math

from random import Random
from dataclasses import dataclass, field
from typing import Type


@dataclass
class Node:
    leaf: bool = False
    value: float = None
    intervals: set = field(default_factory=set)
    enemies: int = 0
    max_enemies: int = 0
    span_left: float = None
    span_right: float = None

    left: Type["Node"] = None
    right: Type["Node"] = None

    @property
    def dot(self):
        span = f"({self.span_left}, {self.span_right})"
        color = "red" if self.leaf else "black"

        dot = f'\t {id(self)} [color={color}, label="id={self.value}\\nleaf={self.leaf}\\nspan={span}\\nintervals={self.intervals}\\nenemies={self.enemies}\\nmax_enemies={self.max_enemies}"] \n'

        if not self.leaf:
            if self.left is not None:
                dot += f'\t {id(self)} -> {id(self.left)}\n'
                dot += self.left.dot
            if self.right is not None:
                dot += f'\t {id(self)} -> {id(self.right)}\n'
                dot += self.right.dot

        return dot


def build_tree(A):
    def _build(A, i, j, l, r):
        if j < i:
            return Node(leaf=True,
                        span_left=l,
                        span_right=r)

        mid = (i + j) // 2
        node = Node(leaf=False,
                    value=A[mid],
                    span_left=l,
                    span_right=r)

        node.left = _build(A, i, mid - 1, l, A[mid])
        node.right = _build(A, mid + 1, j, A[mid], r)

        return node

    A.sort()
    return _build(A, 0, len(A) - 1, -math.inf, math.inf)


def make_enemy(node: Node, l: int, r: int, so_far=0):
    if l <= node.span_left and node.span_right <= r:
        node.intervals.add((l, r))
        node.enemies = so_far + len(node.intervals)
        node.max_enemies = node.enemies
    else:
        so_far += len(node.intervals)

        if l < node.value:
            make_enemy(node.left, l, r, so_far=so_far)
        if node.value < r:
            make_enemy(node.right, l, r, so_far=so_far)

        node.max_enemies = max(node.left.max_enemies,
                               node.right.max_enemies)


def make_good(node: Node, l: int, r: int, so_far=0):
    if l <= node.span_left and node.span_right <= r:
        node.intervals.remove((l, r))
        node.enemies = so_far + len(node.intervals)
        node.max_enemies = node.enemies
    else:
        so_far += len(node.intervals)

        if l < node.value:
            make_good(node.left, l, r, so_far=so_far)
        if node.value < r:
            make_good(node.right, l, r, so_far=so_far)

        node.max_enemies = max(node.left.max_enemies,
                               node.right.max_enemies)


if __name__ == "__main__":
    writers = [(1, 4), (4, 6), (2, 3), (2, 5), (7, 9), (4, 8)]
    years = [l for l, _ in writers] + [r for _, r in writers]
    years = list(set(years))
    root = build_tree(years)

    make_enemy(root, writers[1][0], writers[1][1])
    make_enemy(root, writers[0][0], writers[0][1])
    make_enemy(root, writers[2][0], writers[2][1])

    assert root.max_enemies == 2

    make_good(root, writers[2][0], writers[2][1])

    assert root.max_enemies == 1

    root = build_tree(years)
    enemies = set()

    rand = Random(42)
    for i in range(100):
        l, r = rand.choice(writers)
        enemies.add((l, r))
        make_enemy(root, l, r)

        l, r = rand.choice(writers)
        if (l, r) in enemies:
            enemies.remove((l, r))
            make_good(root, l, r)

    print("digraph {\n" + root.dot + "}")
