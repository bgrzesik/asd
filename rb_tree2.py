from bst_tree import BSTTree, BSTNode

from enum import Enum


class Color(Enum):
    BLACK = 0
    RED = 1


class RBNode(BSTNode):
    def __init__(self, key, value):
        super(RBNode, self).__init__(key, value)
        self.color = Color.BLACK

    def to_str(self, lvl=1):
        tab = lvl * "\t"
        return f"RBNode(\n\
            {tab}\t{self.key} = {self.value},\n\
            {tab}\tcolor = {self.color}\n\
            {tab}\tparent = {self.parent.key if self.parent is not None else None},\n\
            {tab}\tleft = {self.left.to_str(lvl + 1) if self.left is not None else None},\n\
            {tab}\tright = {self.right.to_str(lvl + 1) if self.right is not None else None}\n\
            {tab})"

    @property
    def grandparent(self):
        if self.parent is None:
            return
        return self.parent.parent

    @property
    def uncle(self):
        if self.grandparent is None:
            return None
        elif self.grandparent.left == self.parent:
            return self.grandparent.right
        elif self.grandparent.right == self.parent:
            return self.grandparent.left
        else:
            assert False

    def to_dot(self):
        color = self.color.name.lower()
        dot = f'\t{self.key} [label="{self.key} : {self.value}",color={color}]\n'

        if self.left is not None:
            dot += f"\t{self.key} -- {self.left.key}\n"
            dot += self.left.to_dot()

        if self.right is not None:
            dot += f"\t{self.key} -- {self.right.key}\n"
            dot += self.right.to_dot()

        return dot


class RBTree(BSTTree):
    def __init__(self):
        super(RBTree, self).__init__()

    def put(self, key, value):
        node = RBNode(key, value)
        node.color = Color.RED
        self.put_node(node)
        self.fixup(node)

    def right_rotate(self, y: RBNode):
        x = y.left

        if x is None:
            return

        x.parent = y.parent
        if y == self.root:
            self.root = x
        elif y.parent.left == y:
            y.parent.left = x
        elif y.parent.right == y:
            y.parent.right = x

        y.parent = x

        y.left = x.right
        x.right = y

        if y.left is not None:
            y.left.parent = y

    def left_rotate(self, x: RBNode):
        y = x.right
        if y is None:
            return

        y.parent = x.parent
        if x == self.root:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        elif x.parent.right == x:
            x.parent.right = y

        x.parent = y

        x.right = y.left
        y.left = x

        if x.right is not None:
            x.right.parent = x

    def fixup(self, z: RBNode):
        while z is not None:
            if z == self.root:
                z.color = Color.BLACK                                 # just makin sure
                return
            elif z.parent.color == Color.BLACK:
                return                                                # yo it's fine, end here
            elif z.uncle is not None and z.uncle.color == Color.RED:  # case 1 CLRS
                z.parent.color = Color.BLACK
                z.grandparent.color = Color.RED
                z.uncle.color = Color.BLACK
                z = z.grandparent
            elif z.grandparent.left == z.parent:  # z is on the left of the grandparent
                if z == z.parent.right:
                    """ case 2 CLRS
                           z.grandparent             z.grandparent   
                            /        \                /        \     
                        z.parent    uncle   =>    z.parent    uncle  
                         /    \                     /                
                        *      z                   z                 
                    """
                    self.left_rotate(z.parent)
                    z = z.left

                """ case 3 CLRS          relations before rotation  
                       z.grandparent         z.parent               
                        /        \           /      \               
                    z.parent    uncle  =>   z      z.grandparent    
                      /                               \             
                     z                                uncle         
                """
                z.grandparent.color = Color.RED
                z.parent.color = Color.BLACK
                self.right_rotate(z.grandparent)
                return
            elif z.grandparent.right == z.parent:  # z is on the right of the grandparent
                """ Symetric situations but z is on the right of the grandparent """
                if z == z.parent.left:
                    self.right_rotate(z.parent)
                    z = z.right

                z.grandparent.color = Color.RED
                z.parent.color = Color.BLACK
                self.left_rotate(z.grandparent)
                return

    def __str__(self):
        return f"RBTree({self.root})"

    def to_dot(self):
        dot = "graph RedBlackTree {\n"
        if self.root is not None:
            dot += self.root.to_dot()
        dot += "}"
        return dot


if __name__ == "__main__":
    tree = RBTree()

    tree.put(2, "b")
    tree.put(1, "a")
    tree.put(3, "c")
    tree.put(4, "d")
    tree.put(6, "f")
    tree.put(5, "e")

    print(tree)

    tree = RBTree()

    tree.put(10, "A")
    tree.put(20, "B")
    tree.put(30, "C")

    print(tree)

    tree.put(9, "D")
    tree.put(8, "E")
    tree.put(7, "F")
    tree.put(6, "G")
    tree.put(5, "H")

    print(tree)
    print(tree.to_dot())
