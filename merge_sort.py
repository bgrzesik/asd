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

    def append(self, n):
        i = self

        while i.next is not None:
            i = i.next

        i.next = n


def merge_sort(chain: Node):
    def split(head: Node):
        left = None
        right = None

        pivot = head
        head = head.next
        pivot.next = None

        while head is not None:
            cur = head
            head = head.next
            cur.next = None

            if cur.val <= pivot.val:
                if left is None:
                    left = cur
                else:
                    cur.next = left
                    left = cur
            else:
                if right is None:
                    right = cur
                else:
                    cur.next = right
                    right = cur
        return left, pivot, right

    if chain is None or chain.next is None:
        return chain

    left, pivot, right = split(chain)

    left = merge_sort(left)
    right = merge_sort(right)

    if left is None:
        left = pivot
    else:
        left.append(pivot)

    pivot.next = right

    return left


n = Node(0)
n.add(20)
n.add(40)
n.add(70)
n.add(10)
n.add(50)
n.add(30)
n.add(60)

print(n.arr())

n = merge_sort(n)

print(n.arr())
