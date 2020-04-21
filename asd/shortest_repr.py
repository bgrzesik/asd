
def shortest_repr(S, t):
    f = [None] * (len(t) + 1)
    f[0] = float("inf")

    for i in range(1, len(t) + 1):
        substr = t[:i]

        for s in S:
            if s == substr[-len(s):] and f[i - len(s)] is not None: # is suffix
                n = min(len(s), f[i - len(s)])

                if f[i] is None:
                    f[i] = n
                else:
                    f[i] = min(f[i], n)

    return f[-1]


if __name__ == "__main__":
    print(shortest_repr(["ab", "abab", "ba", "bab", "b"], "ababbab"))
    print(shortest_repr(["makota", "ala", "alam", "ma", "kot", "a"], "alamakota"))
