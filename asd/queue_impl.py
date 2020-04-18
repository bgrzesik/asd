# queue_impl.py because of PyCharm bug

from .stack import Stack

class Queue2(object):
    class Node(object):
        def __init__(self):
            self.val = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        if self.tail is None:
            self.head = self.tail = Queue2.Node()
            self.head.val = val
        else:
            self.tail.next = Queue2.Node()
            self.tail = self.tail.next
            self.tail.val = val

    def dequeue(self):
        val = self.head.val

        self.head = self.head.next
        if self.head is None:
            self.tail = None

        return val

    def is_empty(self):
        return self.head is None


class Queue(object):
    def __init__(self):
        self.ins = Stack()
        self.outs = Stack()

    def enqueue(self, val):
        self.ins.push(val)

    def dequeue(self):
        if self.outs.is_empty():
            while not self.ins.is_empty():
                self.outs.push(self.ins.pop())

        return self.outs.pop()

    def is_empty(self):
        return self.outs.is_empty() and self.ins.is_empty()


if __name__ == "__main__":
    queue = Queue()

    for i in range(10):
        queue.enqueue(i)

    vals = []
    while not queue.is_empty():
        vals.append(queue.dequeue())

    assert vals == list([i for i in range(10)])
