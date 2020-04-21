class Queue5(object):

    def __init__(self):
        self.queues = [[], [], [], [], []]

    def enqueue(self, cost, i, j):  # O(1)
        self.queues[cost - 1].insert(0, (i, j))

    def dequeue(self):  # O(1) i = 0..5
        for i in range(5):
            if len(self.queues[i]) > 0:
                return self.queues[i].pop()
        return None

    def is_empty(self):  # O(1) i = 0..5
        for i in range(5):
            if len(self.queues[i]) > 0:
                return False
        return True


def kings_path(A):
    queues = Queue5()
    n = len(A)

    costs = [[float("inf")] * n for _ in range(n)]

    costs[0][0] = A[0][0]
    queues.enqueue(A[0][0], 0, 0)

    while not queues.is_empty():
        i, j = queues.dequeue()
        cost = float("inf")

        # Zakładam że król porusza się w pionie i poziome, biorąc pod uwagę przykład podany w treści
        # w przeciwnym wypadku używam tabeli jak poniżej
        # (-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, -1), (1, -1), (1, 1),
        for oi, oj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if 0 <= i + oi < n and 0 <= j + oj < n:

                if costs[i + oi][j + oj] != float("inf"):
                    cost = min(cost, costs[i + oi][j + oj])
                else:
                    queues.enqueue(A[i + oi][j + oj], i + oi, j + oj)

        if cost != float("inf"):
            costs[i][j] = A[i][j] + cost

    return costs[n - 1][n - 1]


if __name__ == "__main__":
    A = [[1, 1, 2],
         [5, 1, 3],
         [4, 1, 1]]

    # B = [[1, 1, 1, 5, 5],
    #      [5, 5, 1, 5, 5],
    #      [1, 1, 1, 5, 5],
    #      [1, 5, 5, 5, 5],
    #      [1, 1, 1, 1, 1]]

    print(kings_path(A))  # wypisze 5
    # print( kings_path( B ) ) # wypisze 13
