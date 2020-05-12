
class DoubleLinkedList(object):

    class Node(object):
        def __init__(self, val=None):
            self.prev = None
            self.next = None
            self.key = val

        def delete(self):
            self.prev.next = self.next
            self.next.prev = self.prev

    def __init__(self):
        nil = DoubleLinkedList.Node()
        nil.prev = nil
        nil.next = nil

        self.nil = nil

    def push_front(self, val):
        node = DoubleLinkedList.Node()
        node.key = val

        node.next = self.nil.next
        self.nil.next.prev = node
        self.nil.next = node
        node.prev = self.nil

    def push_back(self, val):
        node = DoubleLinkedList.Node()
        node.key = val

        node.prev = self.nil.prev
        self.nil.prev.next = node
        self.nil.prev = node
        node.next = self.nil

    def _find_node(self, key):
        i = self.nil.next

        while i is not self.nil and i.key == key:
            i = i.next

        return i

    def delete(self, key):
        self._find_node(key).delete()

    def pop_back(self):
        key = self.nil.prev.key
        self.nil.prev.delete()
        return key

    def pop_front(self):
        key = self.nil.next.key
        self.nil.next.delete()
        return key

    def is_empty(self):
        return self.nil.next is self.nil

    def to_arr(self):
        arr = []

        while not self.is_empty():
            arr.append(self.pop_front())

        return arr


if __name__ == "__main__":
    list = DoubleLinkedList()

    list.push_front(10)
    list.push_back(20)

    assert list.pop_back() == 20
    assert list.pop_back() == 10

    assert list.is_empty()

    for i in range(10):
        if i % 2 == 0:
            list.push_front(i)
        else:
            list.push_back(i)

    assert list.to_arr() == [8, 6, 4, 2, 0, 1, 3, 5, 7, 9]
