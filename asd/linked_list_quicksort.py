
class Node:
    def __init__(self):
        self.next = None
        self.val = None


def to_nodes(arr):
    head = Node()
    head.val = arr[0]
    i = head

    for v in range(1, len(arr)):
        i.next = Node()
        i = i.next
        i.val = arr[v]

    return head


def partition(head):
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


def quick_sort(chain):
    if chain is None or chain.next is None:
        return chain, chain

    left, pivot, right = partition(chain)

    left, left_last = quick_sort(left)
    right, right_last = quick_sort(right)

    if left is None or left_last is None:
        left = pivot
    else:
        left_last.next = pivot

    pivot.next = right

    return left, right_last if right_last is not None else pivot


if __name__ == '__main__':
    a, b = quick_sort(to_nodes([1, 2, 3, 4, 5]))

    while a is not None:
        print(a.val)
        a = a.next