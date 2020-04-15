def tasks(A):
    A.sort(key=lambda a: a[1])

    n = 1
    k = 0
    for i in range(1, len(A)):
        if A[i][0] >= A[k][1]:
            k = i
            n += 1

    return n


if __name__ == '__main__':
    print(tasks([(0, 10), (10, 20), (5, 15)]))
