
T = 4


class BTreeNode(object):
    def __init__(self):
        self.children = []
        self.keys = []
        self.leaf = True

    def add_key_non_full(self, k):
        i = 0
        kk = None
        for i, kk in enumerate(self.keys):
            if kk > k:
                break

        if kk is not None and kk < k:
            i += 1

        if self.leaf:
            self.keys.insert(i, k)
        else:
            if len(self.children[i].keys) == 2 * T - 1:
                self.split(i)
                if k > self.keys[i]:
                    i += 1

            self.children[i].add_key_non_full(k)

    def split(self, i):
        y = self.children[i]
        self.keys.insert(i, y.keys[T - 1])

        z = BTreeNode()
        z.leaf = y.leaf
        z.keys = y.keys[T:]
        y.keys = y.keys[:T - 1]

        if not y.leaf:
            z.children = y.children[T:]
            y.children = y.children[:T]

        self.children.insert(i + 1, z)

    def to_dot(self):
        dot = f'\t{id(self)} [label="{self.keys}"]\n'
        for i, child in enumerate(self.children):
            dot += f'\t{id(self)} -- {id(child)} [label="{i}"]\n'
            dot += child.to_dot()
        return dot


class BTree(object):
    def __init__(self):
        self.root = BTreeNode()
        self.root.leaf = True

    def add(self, k):
        if len(self.root.keys) == 2 * T - 1:
            old = self.root
            self.root = BTreeNode()
            self.root.leaf = False
            self.root.children.append(old)
            self.root.split(0)
        self.root.add_key_non_full(k)

    def get(self, k):
        node = self.root
        while node is not None:
            i = 0
            kk = None
            for i, kk in enumerate(node.keys):
                if kk >= k:
                    break

            if i <= len(node.keys) and node.keys[i] == k:
                return k
            elif node.leaf:
                return None
            else:
                if node.keys[-1] < k:
                    i += 1
                node = node.children[i]

    def to_dot(self):
        dot = ""
        if self.root is not None:
            dot = self.root.to_dot()
        return f"graph BTree {{\n{dot}}}"


if __name__ == "__main__":
    from random import Random
    tree = BTree()

    N = 10

    l = list(range(N))
    Random(42).shuffle(l)
    print(l)
    for e in l:
        tree.add(e)

    print(tree.to_dot())

    for i in range(N):
        assert i == tree.get(i)
