import math

from priority_queue import heap_add, heap_pop, heap_peak

from dataclasses import dataclass, field


def shortest(A, k):
    n = len(A)
    A.sort()

    P = []

    for l, r in A:
        extended = False

        for e in P:
            print(l, r, e)
            if e[-1][1] <= l and len(e) < k:
                e.append((l, r))
                extended = True
                break
            elif len(e) >= k and e[-1][1] <= l and e[-1][1] - e[0][0] >= r - e[1][0]:
                e.pop(0)
                e.append((l, r))
                extended = True
                break
            elif len(e) >= k and e[-1][1] >= r and e[-1][1] - e[0][0] >= r - e[0][0]:
                e.pop()
                e.append((l, r))
                extended = True
                break

        if not extended:
            P.append([(l, r)])

    a = math.inf
    r = None

    print(P)

    for i in range(len(P)):
        if len(P[i]) == k and a > P[i][-1][1] - P[i][0][0]:
            r = i
            a = P[i][-1][1] - P[i][0][0]

    if r is not None:
        return P[r]
    return None


def shortest2(A, k):
    queue = []
    heap_add(queue, (-A[0][1], [A[0]]))

    result = None
    A.sort()

    for l, r in A[1:]:
        if (-heap_peak(queue)[0]) > l:
            heap_add(queue, (-r, [(l, r)]))
            continue

        while (-heap_peak(queue)[0]) <= l:
            _, li = heap_pop(queue)

            if len(li) < k:
                li.append((l, r))
            else:
                if result is None or (result[-1][1] - result[0][0]) > (li[-1][1] - li[0][0]):
                    result = li.copy()
                li.pop(0)
                li.append((l, r))

            heap_add(queue, (-r, li))

    for _, li in queue:
        if len(li) != k:
            continue

        if result is None or (result[-1][1] - result[0][0]) > (li[-1][1] - li[0][0]):
            result = li.copy()

    return result


if __name__ == "__main__":
    # print(shortest([(0, 2), (1, 5), (2, 3), (3, 9), (5, 6), (7, 9)], 3))

    print(shortest2([(0, 3), (1, 5), (2, 6), (4, 8), (7, 10), (9, 11)], 3))

    print(shortest2([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6)], 3))
