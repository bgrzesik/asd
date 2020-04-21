def insert_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > val:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = val


class Node:
    def __init__(self, val=None):
        self.next = None
        self.val = None


def insert_sort_linked_list(head):
    node = head
    res = Node()

    while node.next is not None:
        i = node.next
        node.next = node.next.next

        j = res
        while j.next is not None and j.next.val < i.val:
            j = j.next

        i.next = j.next
        j.next = i

    head.next = res.next
    return head


if __name__ == "__main__":
    tab = [0, 0, 2, 3, 4, 1, 3, 3, 3, 4, 5]
    insert_sort(tab)
    assert tab == list(sorted([0, 0, 2, 3, 4, 1, 3, 3, 3, 4, 5]))

    head = Node()
    for i in [0, 2, 4, 6, 7, 8, 3, 4, 5, 3, 1, 12, 24, 56]:
        node = Node()
        node.val = i
        node.next = head.next
        head.next = node

    insert_sort_linked_list(head)

    arr = []
    while head.next is not None:
        node = head.next
        head.next = head.next.next
        arr.append(node.val)

    assert arr == [0, 1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 12, 24, 56]