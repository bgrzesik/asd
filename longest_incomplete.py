
def set_add(s, v):
    i = 0
    idx = v % len(s)

    while s[idx] is not None:
        idx += 1
        idx %= len(s)
        i += 1

        if i >= len(s):
            raise ValueError

    s[idx] = v


def set_has(s, v):
    i = 0
    idx = v % len(s)

    while s[idx] is not None and s[idx] != v:
        idx += 1
        idx %= len(s)
        i += 1

        if i >= len(s):
            return False

    return s[idx] == v


def longest_incomplete(A, k):
    def longest_mid(low, mid, high):
        nonlocal A, k
        s = [None] * k
        n = 0
        d = 0

        l = mid
        for l in range(mid, low - 1, -1):
            v = A[l]
            has = set_has(s, v)

            if not has and d + 1 < k:
                n += 1
                d += 1
                set_add(s, v)
            elif not has:
                l += 1
                break
            else:
                n += 1

        # l -= 1

        r = mid + 1
        for r in range(mid + 1, high + 1):
            v = A[r]
            has = set_has(s, v)

            if not has and d + 1 < k:
                n += 1
                d += 1
                set_add(s, v)
            elif not has:
                r -= 1
                break
            else:
                n += 1

        # r -= 1

        # assert r - l == n
        return (n, l, r)

    def longest(low, high):
        nonlocal A, k

        if low >= high:
            assert low == high
            return (1, low, high)

        mid = (low + high) // 2

        return max(
            longest(low, mid),
            longest(mid + 1, high),
            longest_mid(low, mid, high)
        )

    return longest(0, len(A) - 1)


if __name__ == "__main__":
    s = [None] * 3

    set_add(s, 5)

    assert set_has(s, 5)
    assert not set_has(s, 100)
    assert not set_has(s, 3)

    set_add(s, 100)
    assert set_has(s, 5)
    assert set_has(s, 100)
    assert not set_has(s, 3)

    set_add(s, 3)
    assert set_has(s, 5)
    assert set_has(s, 100)
    assert set_has(s, 3)

    A = [1, 100, 5, 100, 1, 5, 1, 5]
    n, low, high = longest_incomplete(A, 3)
    assert (n, A[low:high + 1]) == (4, [1, 5, 1, 5])

    A = [1, 100, 1, 5, 1, 5, 100, 5]
    n, low, high = longest_incomplete(A, 3)
    assert (n, A[low:high + 1]) == (4, [1, 5, 1, 5])

    A = [1, 5, 1, 5, 100, 5, 1, 100]
    n, low, high = longest_incomplete(A, 3)
    assert (n, A[low:high + 1]) == (4, [1, 5, 1, 5])
