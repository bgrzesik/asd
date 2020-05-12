from math import floor


class Node(object):
    def __init__(self, val=None):
        self.val = None
        self.next = None

    @staticmethod
    def to_list(arr):
        head = Node()
        for e in arr:
            node = Node()
            node.val = e
            node.next = head.next
            head.next = node
        return head

    def to_array(self):
        arr = []

        while self.next is not None:
            node = self.next
            self.next = self.next.next
            arr.append(node.val)

        return arr


def insert_sort(head):
    res = Node()
    node = head

    end = head

    while node.next is not None:
        i = node.next
        node.next = node.next.next

        j = res
        while j.next is not None and j.next.val < i.val:
            j = j.next

        i.next = j.next
        j.next = i

        if end is head or end.val < i.val:
            end = i

    head.next = res.next
    return end


def sort_floats_linked_list(head):
    buckets = [Node() for i in range(10)]
    node = head

    while node.next is not None:
        i = node.next
        node.next = node.next.next

        j = buckets[floor(i.val)]
        i.next = j.next
        j.next = i

    start = buckets[0]
    end = insert_sort(buckets[0])

    for i in range(1, 10):
        bucket = buckets[i]
        bucket_end = insert_sort(bucket)

        end.next = bucket.next

        if bucket.next is not None:
            end = bucket_end

    return start


if __name__ == "__main__":
    head = Node.to_list([1.6, 9.23, 9.1, 9.3, 2.3, 3.4, 4.4, 5.5, 4.1])
    head = sort_floats_linked_list(head)
    assert head.to_array() == [1.6, 2.3, 3.4, 4.1, 4.4, 5.5, 9.1, 9.23, 9.3]
