class Node(object):
    def __init__(self):
        self.next = None
        self.value = None

    @staticmethod
    def from_array(array):
        head = None
        for i in range(len(array) - 1, -1, -1):
            node = Node()
            node.value = array[i]
            node.next = head
            head = node

        return head

    def to_array(self):
        arr = [self.value]
        while self.next is not None:
            arr.append(self.next.value)
            self.next = self.next.next
        return arr


def fix_sorted_list(head):
    prev = None
    node = head
    next = head.next.value

    while node is not None:
        left = float("-inf")
        if prev is not None:
            left = prev.value

        if not (left <= node.value <= next) and left < next:
            break
        else:
            prev = node

            node = node.next
            if node is None:
                break

            if node.next is not None:
                next = node.next.value
            else:
                next = float("+inf")

    if prev is not None:
        prev.next = node.next
    else:
        head = head.next

    nil = Node()
    nil.next = head

    i = nil
    while i.next is not None and i.next.value < node.value:
        i = i.next

    node.next = i.next
    i.next = node

    return nil.next


if __name__ == "__main__":
    head = Node.from_array([1, 2, 3, 4, 5, 9, 7, 8, 9, 10, 11])
    fix_sorted_list(head)
    assert head.to_array() == [1, 2, 3, 4, 5, 7, 8, 9, 9, 10, 11]
