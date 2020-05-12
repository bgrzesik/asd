from math import sqrt, floor, ceil


def sort_points(arr, k):
    buckets = [[] for _ in range(ceil(sqrt(k) + 1))]

    for x, y, in arr:
        idx = floor(sqrt(x ** 2 + y ** 2))
        buckets[idx].append((x, y))

    for bucket in buckets:
        for i in range(1, len(bucket)):

            x, y = bucket[i]
            d = sqrt(x ** 2 + y ** 2)

            j = i - 1
            while j >= 0 and d < sqrt(bucket[j][0] ** 2 + bucket[j][1] ** 2):
                bucket[j + 1] = bucket[j]
                j -= 1

            bucket[j + 1] = (x, y)

    i = 0
    for bucket in buckets:
        for x, y in bucket:
            arr[i] = (x, y)
            i += 1

    return arr


if __name__ == "__main__":
    print(sort_points([(1, 1), (2, 0), (0, 2), (0, 0), (0.5, 0.5)], 2))
