class LinkedList(object):
    class Node(object):
        def __init__(self, val=None, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = LinkedList.Node()

    def add(self, val):
        n = LinkedList.Node()
        n.val = val
        n.next = self.head.next
        self.head.next = n

    @staticmethod
    def from_list(tab):
        li = LinkedList()

        node = li.head

        for i in range(len(tab)):
            node.next = LinkedList.Node()
            node.next.val = tab[i]
            node = node.next

        return li

    def to_list(self):
        l = []

        n = self.head

        while n.next is not None:
            n = n.next
            l.append(n.val)

        return l

    def sort(self):
        def _sort(node):
            if node.next is None:
                return node, node

            pivot = node.next
            pivot_end = pivot

            node.next = pivot.next  # remove pivot from the list
            pivot.next = None

            left = LinkedList.Node()
            left_end = left
            right = LinkedList.Node()
            right_end = right

            while node.next is not None:
                nn = node.next
                node.next = None
                node = nn

                if node.val == pivot.val:
                    pivot_end.next = node
                    pivot_end = pivot_end.next
                elif node.val < pivot.val:
                    left_end.next = node
                    left_end = left_end.next
                elif node.val > pivot.val:
                    right_end.next = node
                    right_end = right_end.next

            left, left_end = _sort(left)
            right, right_end = _sort(right)

            left_end.next = pivot
            pivot_end.next = right.next

            if right.next is None:
                return left, pivot_end

            return left, right_end

        head, end = _sort(self.head)
        self.head = head


if __name__ == '__main__':
    assert LinkedList.from_list([0, 1, 2, 3, 4, 5]).to_list() == [0, 1, 2, 3, 4, 5]

    ll = LinkedList.from_list([6, 5, 1, 2, 3, 0, 4])
    ll.sort()
    assert ll.to_list() == [0, 1, 2, 3, 4, 5, 6]
