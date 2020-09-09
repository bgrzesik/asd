
from typing import Type
from dataclasses import dataclass


@dataclass
class Node:
    value: int = None
    left: Type["Node"] = None
    right: Type["Node"] = None

    @property
    def dot(self):
        dot = f"{id(self)} [label=\"{self.value}\"]\n"

        if self.left:
            dot += f"{id(self)} -- {id(self.left)}\n{self.left.dot}\n"
        if self.right:
            dot += f"{id(self)} -- {id(self.right)}\n{self.right.dot}\n"

        return dot


def consturct(arr):
    arr.sort()

    def new(lo, hi):
        nonlocal arr

        if lo > hi:
            return None

        mid = (lo + hi) // 2

        return Node(value=arr[mid],
                    left=new(lo, mid - 1),
                    right=new(mid + 1, hi))

    return new(0, len(arr) - 1)


def serialize(root: Node):
    arr = []
    stack = [root]

    while stack:
        node = stack.pop(0)

        if node is not None:
            arr.append(node.value)
            stack.insert(0, node.left)
            stack.insert(1, node.right)
        else:
            arr.append(None)

    return arr


# def deserialize(arr):

#     if arr[0] is None:
#         return None, 1

#     node = Node(value=arr[0])
#     node.left, off = deserialize(arr[1:])
#     node.right, off2 = deserialize(arr[1 + off:])

#     return node, 1 + off + off2

def deserialize(arr):
    root = Node(value=arr[0])
    stack = [root]

    for i in range(1, len(arr) - 1):

        if arr[i] is None:
            if arr[i + 1] is None:
                stack.pop(0)
            continue

        node = Node(value=arr[i])
        if arr[i] < stack[0].value:
            stack[0].left = node
            stack.insert(0, node)
        else:
            stack[0].right = node
            stack.pop(0)
            stack.insert(0, node)

    return root


if __name__ == "__main__":
    root = consturct([0, 1, 2, 3, 4, 5, 6, 7])

    # print(root.dot)
    print(serialize(root))
    print(deserialize([3, 1, 0, None, None, 2, None, None,
                       5, 4, None, None, 6, None, 7, None, None]).dot)
