def find_most_occurring(str, k):
    n = 2 ** k
    count = [0] * n

    num = 0

    for i in range(k - 1):
        if str[i] == "b":
            num |= 1
        num <<= 1

    idx = 0
    for i in range(k - 1, len(str)):
        if str[i] == "b":
            num |= 1

        count[num] += 1

        if count[num] > count[idx]:
            idx = num

        num <<= 1
        num &= ((1 << k) - 1)

    pattern = ["a"] * k
    for i in range(k - 1, -1, -1):
        if (idx & 1) != 0:
            pattern[i] = "b"
        idx >>= 1

    return "".join(pattern)


def find_most_occurring2(word, k, e):
    max_idx = 0
    max_count = 0

    num = 0
    for i in range(k - 1):
        num += word[i]
        num *= e

    for i in range(k - 1, len(word)):
        num += word[i] % e

        word[num] += e
        if max_count < (word[num] // e):
            max_count = (word[num] // e)
            max_idx = i

        num *= e
        num %= e ** k

    for i in range(0, len(word)):
        word[i] %= e

    return word[max_idx - k + 1: max_idx + 1]


if __name__ == "__main__":
    assert find_most_occurring("ababaaaabb", 3) in ["aaa", "aba"]
    assert find_most_occurring("ababbbbbabababab", 4) in ["abab"]
    assert find_most_occurring("ababbbbbaabababab", 4) in ["abab"]
    assert find_most_occurring2([0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1], 4, 2) == [0, 1, 0, 1]
    l = [0, 1, 2, 0, 1, 2, 2, 1, 0,
         2, 2, 2, 0, 0, 0, 0, 1, 2,
         2, 1, 0, 2, 1, 0, 0, 1, 2]
    assert find_most_occurring2(l, 3, 3) == [0, 1, 2]
