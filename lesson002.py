def _parent(i):
    return (i - 1) // 2

def _left(i):
    return 2 * i + 1


def _right(i):
    return 2 * i + 2


class Heap:

    def __init__(self, arr):

        if arr is not None:
            self.arr = arr[:]

            for i in range((len(arr) // 2) - 1, -1, -1):
                self.heapify(i)
        else:
            self.arr = []

    def heapify(self, i):
        left = _left(i)
        right = _right(i)

        largest = i

        if left < len(self.arr) and self.arr[left] > self.arr[i]:
            largest = left

        if right < len(self.arr) and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != i:
            self.swap(i, largest)

            self.heapify(largest)

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    @property
    def head(self):
        return self.arr[0]

    def extract_top(self):
        top = self.arr[0]
        self.swap(0, len(self.arr) - 1)
        self.arr.pop()
        self.heapify(0)
        return top




def heapsort(arr):
    heap = Heap(arr=arr)
    dest = []

    for i in range(len(arr)):
        dest.insert(0, heap.extract_top())

    return dest


if __name__ == "__main__":
    arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
    heap = Heap(arr=arr)
    print(heap.arr)

    print(heapsort(arr))



