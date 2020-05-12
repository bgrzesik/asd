
class MaxHeap(object):

    @staticmethod
    def _parent(i):
        return (i - 1) // 2

    @staticmethod
    def _left(i):
        return 2 * i + 1

    @staticmethod
    def _right(i):
        return 2 * i + 2


    def __init__(self):
        self.arr = []

    def build(self, arr):
        self.arr = arr
        for i in range(MaxHeap._parent(len(self.arr)), -1 , -1):
            self.heapify(i)

    def heapify(self, i):
        l = MaxHeap._left(i)
        r = MaxHeap._right(i)

        largest = i

        if l < len(self.arr) and self.arr[largest] < self.arr[l]:
            largest = l
        if r < len(self.arr) and  self.arr[largest] < self.arr[r]:
            largest = r

        if largest != i:
            self.arr[largest], self.arr[i] = self.arr[i], self.arr[largest]
            self.heapify(largest)

    def extract_top(self):
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        val = self.arr.pop()
        self.heapify(0)
        return val

    def insert(self, val):
        self.arr.append(val)

        i = len(self.arr) - 1

        while i > 0 and self.arr[i] > self.arr[MaxHeap._parent(i)]:
            p = MaxHeap._parent(i)
            self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            i = p

    @staticmethod
    def heapsort(arr):
        heap = MaxHeap()
        heap.build(arr)

        arr = [heap.extract_top() for _ in range(len(heap.arr))]

        for i in range(len(arr) // 2):
            arr[i], arr[-(i + 1)] =  arr[-(i + 1)], arr[i]

        return arr


if __name__ == "__main__":
    heap = MaxHeap()

    for i in range(6):
        heap.insert(i)

    test = [17, 15, 13, 9, 6, 5, 10, 4, 8, 3, 1]
    MaxHeap.heapsort(test), heap.arr
