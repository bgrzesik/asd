class BSTNode(object):
    def __init__(self, key=None):
        self.key = key
        self.parent: BSTNode = None
        self.left: BSTNode = None
        self.right: BSTNode = None
        self.color = None

    def succ(self):
        if self.right is not None:
            return self.right.min()

        x = self
        y = self.parent

        while y is not None and y.right is x:
            x = y
            y = y.parent

        return y

    def pred(self):
        if self.left is not None:
            return self.left.max()

        x = self
        y = self.parent

        while y is not None and y.left is x:
            x = y
            y = y.parent

        return y

    def max(self):
        node = self
        while node.right is not None:
            node = node.right
        return node

    def min(self):
        node = self
        while node.left is not None:
            node = node.left
        return node


class BSTTree(object):
    def __init__(self):
        self.root: BSTNode = None

    def add(self, key):
        self.add_node(BSTNode(key))

    def add_node(self, z: BSTNode):
        y = None
        x = self.root

        while x is not None:
            y = x

            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def find(self, key):
        node = self.root

        while node is not None and node.key != key:
            if node.key < key:
                node = node.left
            else:
                node = node.right

        return node

    def remove(self, key):
        self.remove_node(self.find(key))

    def remove_node(self, z: BSTNode):
        if z.left is None:
            self.put_in_place(z, z.right)
        elif z.right is None:
            self.put_in_place(z, z.left)
        else:
            y = z.right.min()
            if y.parent is not z:
                self.put_in_place(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.put_in_place(z, y)
            y.left = z.left
            y.left.parent = y

    def put_in_place(self, u, v):
        if u is self.root:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent


if __name__ == "__main__":
    tree = BSTTree()
    tree.add(10)
    tree.add(15)
    tree.add(5)
    tree.add(1)

    tree.remove(10)

    print(tree)
