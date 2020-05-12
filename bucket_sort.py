def bucket_sort(tab, k):
    b = [[] for i in range(k)]

    for el in tab:
        b[int(k * el)].append(el)

    for i in range(k):
        b[i].sort()

    res = []

    for t in b:
        res.extend(t)

    return res


if __name__ == "__main__":
    tab = [0.1, 0.25, 0.2, 0.3, 0.11, 0.14, 0.6, 0.7, 0.3, 0.4]
    bucket_sort(tab, len(tab) // 2)
