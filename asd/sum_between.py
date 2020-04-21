from asd.medians_of_medians import quicker_select


def sum_between(arr, from_, to):
    from_ = quicker_select(arr, from_)
    to = quicker_select(arr, to - from_, p=from_)

    return sum(arr[from_:to + 1])


if __name__ == "__main__":
    l = [8, 0, 4, 5, 1, 2, 3, 6, 7]
    s = sum_between(l.copy(), 2, 4)
    l.sort()
    assert s == 6

    l = [8, 0, 4, 5, 1, 2, 3, 6, 7]
    s = sum_between(l.copy(), 4, 6)
    l.sort()
    assert s == 12
