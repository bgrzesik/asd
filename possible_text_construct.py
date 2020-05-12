


def possible(u, v, w):
    counts = [0] * 26

    for c in u:
        counts[ord(c) - ord('a')] += 1

    for c in v:
        counts[ord(c) - ord('a')] += 1

    for c in w:
        if counts[ord(c) - ord('a')] > 0:
            counts[ord(c) - ord('a')] -= 1
        else:
            return False

    return True


if __name__ == "__main__":
    assert possible("alama", "akot", "alamakota")
    assert not possible("alam", "akot", "alamakota")
