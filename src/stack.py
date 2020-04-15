
class Stack(object):
    class Node(object):
        def __init__(self):
            self.val = None
            self.next = None

    def __init__(self):
        self.top = Stack.Node()

    def push(self, val):
        n = Stack.Node()
        n.val = val
        n.next = self.top
        self.top = n

    def pop(self):
        val = self.top.val

        if self.top.next is None:
            print("Stos jest pusty")
            return None

        self.top = self.top.next
        return val

    def is_empty(self):
        return self.top.next is None


if __name__ == "__main__":
    stack = Stack()
    for i in range(10):
        stack.push(i)

    vals = []
    while not stack.is_empty():
        vals.append(stack.pop())

    assert vals == list([i for i in range(9, -1, -1)])
