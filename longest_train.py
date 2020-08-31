
def _find(unions, i):
    while i != unions[i][0]:
        unions[i] = unions[unions[i][0]]
        i = unions[i][0]
    return unions[i]


def _union(unions, i, j):
    i, i_rank = _find(unions, i)
    j, j_rank = _find(unions, j)

    if i_rank > j_rank:
        unions[i][1] = i_rank + j_rank
        unions[j][0] = i
    else:
        unions[j][1] = i_rank + j_rank
        unions[i][0] = j


def longest_train(ids, conns):
    unions = {i: [i, 1] for i in ids}

    for a, b in conns:
        _union(unions, a, b)

    return max(unions.values(), key=lambda e: e[1])[1]


if __name__ == "__main__":
    ids = [404, 42, 666, 69, -1, 13, 7]
    conns = [(404, 42), (666, 69), (42, 666), (13, 7), (69, -1)]

    print(longest_train(ids, conns))
