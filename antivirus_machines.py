

def placement(A, k):
    i = 0
    m = 0
    while i + k < len(A):
        l = i
        for j in range(min(i + k, len(A) - 1), i, -1):
            if A[j] == 1:
                i = j
                m += 1
                break
        if i == l:
            return None

    return m


if __name__ == "__main__":
    print(placement([0, 0, 1, 0, 0, 1, 0, 0, 1], 3))
    print(placement([0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1], 3))
    print(placement([0, 0, 0, 0, 0, 1, 0, 0, 1], 3))
