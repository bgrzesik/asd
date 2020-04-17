from math import log2, floor
# from operator import gt, lt

def _parent(i):
    # 1 -> 0
    # 2 -> 0
    # 3 -> 1
    # 4 -> 1
    # 5 -> 2
    return (i - 1) // 2


def _left(i):
    return i * 2 + 1


def _right(i):
    return i * 2 + 2


def _grandparent(i):
    return _parent(_parent(i))


def _has_grandparent(i):
    #   0
    #  1 2
    # 3
    return i >= 3

def _level(i):
    return floor(log2(i + 1))


def _is_min_level(i):
    return _level(i) % 2 == 0


def _is_grandchild(grandparent, grandchild):
    return _parent(_parent(grandchild)) == grandparent


class Heap(object):

    def __init__(self):
        self.arr = []

    @staticmethod
    def from_array(array):
        heap = Heap()
        heap.arr = array

        for i in range(_parent(len(array)), -1, -1):
            heap.push_down(i)

        return heap

    def push_down(self, i):
        if _is_min_level(i):
            self._push_down_min(i)
        else:
            self._push_down_max(i)

    def _push_down_min(self, i):
        if not self._has_children(i):
            return

        m = self._smallest_child_grandchild(i)

        if _is_grandchild(i, m):
            if self.arr[m] < self.arr[i]:
                self.arr[m], self.arr[i] = self.arr[i], self.arr[m]

                if self.arr[m] > self.arr[_parent(m)]:
                    self.arr[m], self.arr[_parent(m)] = self.arr[_parent(m)], self.arr[m]

                self._push_down_min(m)

        elif self.arr[m] < self.arr[i]:
            self.arr[m], self.arr[i] = self.arr[i], self.arr[m]

    def _push_down_max(self, i):
        if not self._has_children(i):
            return

        m = self._largest_child_grandchild(i)

        if _is_grandchild(i, m):
            if self.arr[m] > self.arr[i]:
                self.arr[m], self.arr[i] = self.arr[i], self.arr[m]

                if self.arr[m] < self.arr[_parent(m)]:
                    self.arr[m], self.arr[_parent(m)] = self.arr[_parent(m)], self.arr[m]

                self._push_down_min(m)

        elif self.arr[m] > self.arr[i]:
            self.arr[m], self.arr[i] = self.arr[i], self.arr[m]

    def _has_children(self, i):
        return _left(i) < len(self.arr)

    def _smallest_child_grandchild(self, i):
        return min(self._child_grandchild(i), key=lambda e: self.arr[e])

    def _largest_child_grandchild(self, i):
        return max(self._child_grandchild(i), key=lambda e: self.arr[e])

    def _child_grandchild(self, i):
        arr = [
            _left(i), _left(_left(i)), _right(_left(i)),
            _right(i), _left(_right(i)), _right(_right(i)),
        ]
        return filter(lambda e: 0 < e < len(self.arr), arr)

    def extract_min(self):
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]

        minimum = self.arr.pop()
        self.push_down(0)

        return minimum

    def extract_max(self):
        if len(self.arr) == 1:
            return self.arr.pop()

        i = 1
        if len(self.arr) >= 3 and self.arr[1] < self.arr[2]:
            i = 2

        self.arr[i], self.arr[-1] = self.arr[-1], self.arr[i]
        maximum = self.arr.pop()
        self.push_down(i)

        return maximum

    def insert(self, val):
        self.arr.append(val)
        self.push_up(len(self.arr) - 1)

    def push_up(self, i):
        if i == 0:
            return

        if _is_min_level(i):
            if self.arr[i] > self.arr[_parent(i)]:
                self.arr[i], self.arr[_parent(i)] = self.arr[_parent(i)], self.arr[i]
                self._push_up_max(_parent(i))
            else:
                self._push_up_min(i)
        else:
            if self.arr[i] < self.arr[_parent(i)]:
                self.arr[i], self.arr[_parent(i)] = self.arr[_parent(i)], self.arr[i]
                self._push_up_min(_parent(i))
            else:
                self._push_up_max(i)

    def _push_up_min(self, i):
        while _has_grandparent(i) and self.arr[i] < self.arr[_grandparent(i)]:
            self.arr[i], self.arr[_grandparent(i)] = self.arr[_grandparent(i)], self.arr[i]
            i = _grandparent(i)

    def _push_up_max(self, i):
        while _has_grandparent(i) and self.arr[i] > self.arr[_grandparent(i)]:
            self.arr[i], self.arr[_grandparent(i)] = self.arr[_grandparent(i)], self.arr[i]
            i = _grandparent(i)

if __name__ == '__main__':
    assert _is_min_level(0)
    assert not _is_min_level(2)
    assert _is_min_level(6)
    assert not _is_min_level(7)

    assert not _is_grandchild(0, 1)
    assert _is_grandchild(0, 3)
    assert _is_grandchild(1, 8)

    heap = Heap.from_array([5, 4, 3, 2, 1, 0])

    assert heap.arr == [0, 4, 5, 2, 1, 3]

    heap.insert(6)

    assert heap.arr == [0, 4, 6, 2, 1, 3, 5]

    assert heap.extract_max() == 6
    assert heap.extract_min() == 0

    assert heap.arr == [1, 4, 5, 2, 3]

    assert heap.extract_min() == 1
    assert heap.extract_max() == 5

    assert heap.extract_min() == 2
    assert heap.extract_max() == 4

    assert heap.extract_min() == 3
