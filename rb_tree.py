
from enum import Enum
from bst_tree import BSTNode, BSTTree


class Color(Enum):
    BLACK = 0
    RED = 1


class RBTree(BSTTree):
    def left_rotate(self, x: BSTNode):
        y = x.right
        x.right = y.left

        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent

        if x is self.root:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        elif x is x.parent.right:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x: BSTNode):
        y = x.left
        x.left = y.right

        if y.right is not None:
            y.right.parent = x

        y.parent = x.parent

        if x is self.root:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        elif x is x.parent.right:
            x.parent.right = y

        y.right = x
        x.parent = y

    def add_node(self, z: BSTNode):
        super().add_node(z)
        z.color = Color.RED
        self.fix(z)

    def fix(self, z):
        while z.parent.color == Color.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right

                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent

                elif z is z.parent.right:
                    z = z.parent
                    self.left_rotate(z)
                z.parent.color = Color.BLACK
                z.parent.parent.color = Color.RED
                self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left

                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent

                elif z is z.parent.left:
                    z = z.parent
                    self.left_rotate(z)
                z.parent.color = Color.BLACK
                z.parent.parent.color = Color.RED
                self.right_rotate(z.parent.parent)

        self.root.color = Color.BLACK


if __name__ == "__main__":
    pass
