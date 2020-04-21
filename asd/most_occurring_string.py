
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


if __name__ == "__main__":
    assert find_most_occurring("ababaaaabb", 3) in ["aaa", "aba"]
    assert find_most_occurring("ababbbbbabababab", 4) in ["abab"]
    assert find_most_occurring("ababbbbbaabababab", 4) in ["abab"]
