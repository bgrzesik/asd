import math


class SegmentTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.segments = set()

        self.parent = None
        self.left = None
        self.right = None

    def min(self):
        i = self
        while i.left is not None:
            i = i.left
        return i

    def max(self):
        i = self
        while i.right is not None:
            i = i.right
        return i

    def succ(self):
        if self.right is not None:
            return self.right.min()

        i = self
        while i.parent is not None and i == i.parent.right:
            i = i.parent

        return i.parent

    def pred(self):
        if self.left is not None:
            return self.left.max()

        i = self
        while i.parent is not None and i == i.parent.left:
            i = i.parent

        return i.parent

    def span_end(self):
        end = self
        while end.parent is not None and end == end.parent.right:
            end = end.parent
        end = end.parent
        return end.value if end is not None and end.value is not None else math.inf

    def span_start(self):
        start = self
        while start.parent is not None and start == start.parent.left:
            start = start.parent
        start = start.parent
        return start.value if start is not None and start.value is not None else -math.inf

    def span(self):
        return (self.span_start(), self.span_end())

    def to_dot(self):
        dot = f'\t{id(self)} [label="{self.value} {self.span()} \\n {self.segments}"]\n'

        if self.left is not None:
            dot += f"\t{id(self)} -- {id(self.left)}\n"
            dot += self.left.to_dot()

        if self.right is not None:
            dot += f"\t{id(self)} -- {id(self.right)}\n"
            dot += self.right.to_dot()

        return dot

    def __str__(self):
        return f"SegmentTreeNode({self.value} {self.segments})"


class SegmentTree(object):

    def __init__(self):
        self.root = SegmentTreeNode(None)

    def _insert_node(self, v):
        i = self.root
        while i is not None:
            if i.value == v:
                break

            elif i.value == None:
                i.value = v
                i.left = SegmentTreeNode(None)
                i.left.parent = i
                i.right = SegmentTreeNode(None)
                i.right.parent = i
                break

            elif i.value > v:
                i = i.left

            elif i.value < v:
                i = i.right

    def put(self, start, end, data):
        self._insert_node(start)
        self._insert_node(end)
        self._put(self.root, start, end, data)

    def _remove(self, i, start, end):
        if start <= i.span_start() and i.span_end() <= end:
            f = filter(lambda i: i[0] == start and i[1] == end, i.segments)
            r = next(f)
            i.segments.discard(r)

        elif i.value <= start:
            self._remove(i.right, start, end)

        elif end <= i.value:
            self._remove(i.left, start, end)

        elif start <= i.value <= end:
            self._remove(i.left, start, end)
            self._remove(i.right, start, end)

        else:
            assert False

    def _put(self, i, start, end, data):
        if start <= i.span_start() and i.span_end() <= end:
            i.segments.add((start, end, data))

        else:
            if start < i.value:
                self._put(i.left, start, end, data)
            if i.value < end:
                self._put(i.right, start, end, data)

    def get(self, p):
        i = self.root
        r = set()

        while i is not None:
            if i.span_start() <= p <= i.span_end():
                r.update(i.segments)

            if i.value is None or i.value < p:
                i = i.right
            elif i.value > p:
                i = i.left
            else:
                j = i.left
                while j is not None:
                    r.update(j.segments)
                    j = j.right

                i = i.right

        return r

    def remove(self, start, end):
        self._remove(self.root, start, end)

    def to_dot(self):
        return "graph Segment {\n" + self.root.to_dot() + "\n}"


if __name__ == "__main__":
    tree = SegmentTree()
    tree.put(0, 1, "A")
    tree.put(1, 2, "B")

    print(tree.to_dot())

    tree.put(0, 2, "B")
    tree.put(-2, 2, "B")

    print(tree.to_dot())

    print(tree.get(1))
    print(tree.get(1.1))

    tree.remove(-2, 2)
    print(tree.get(1))

    intervals = [(1, 3), (4, 6), (7, 8), (2, 4), (5, 8), (3, 6)]

    tree = SegmentTree()
    result = 0

    for (a, b) in intervals:
        n = 0

        col = tree.get(a + 0.0001) | tree.get(b - 0.0001)
        for (start, end, data) in col:
            tree.remove(start, end)

            if start != a:
                tree.put(start, a, data)

            if end != b:
                tree.put(b, end, data)

            n = max(n, data)

        print(a, b, col, n)

        tree.put(a, b, n + 1)
        result = max(result, n + 1)

    print(tree.to_dot())
    print(result)
