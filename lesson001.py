class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def add(self, val):
        old_val = self.val
        self.val = val
        self.next = Node(old_val, self.next)

    def arr(self):
        arr = [self.val]
        i = self.next

        while i is not None:
            arr.append(i.val)
            i = i.next

        return arr


# Porównać algorytmy
# Odwracanie listy
# Przesuwanie o k elementów
# lista kolorów znaleźć najdłuższy podciąg zawierający wszystkie kolory


def insert_sort(node):
    start = Node(next=None)

    i = node
    while i is not None:
        curr = i
        i = i.next

        e = start
        while e.next is not None and e.next.val < curr.val:
            e = e.next

        last = e.next
        e.next = curr
        curr.next = last

    return start.next


def reveeee(node):
    last = node
    node = node.next
    last.next = None

    while node is not None:
        nn = node.next

        node.next = last
        last = node
        node = nn

    return last


if __name__ == "__main__":
    a = Node(val=1)
    a.add(2)
    a.add(3)
    a.add(4)
    a.add(-10)
    a.add(200)
    a.add(5)
    a.add(6)

    print(a.arr())
    a = insert_sort(a)
    print(a.arr())
    a = reveeee(a)
    print(a.arr())
