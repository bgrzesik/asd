def count_sort(arr, arr2, idx, reverse):
    counts = [0] * 10

    for i in range(len(arr)):
        counts[arr[i][idx]] += 1

    if not reverse:
        for i in range(1, len(counts)):
            counts[i] += counts[i - 1]
    else:
        for i in range(len(counts) - 2, -1, -1):
            counts[i] += counts[i + 1]

    buf = [None] * len(arr)
    buf2 = [None] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        val = arr[i][idx]

        counts[val] -= 1
        buf[counts[val]] = arr[i]
        buf2[counts[val]] = arr2[i]

    for i in range(len(arr)):
        arr[i] = buf[i]
        arr2[i] = buf2[i]


def convert(num):
    counts = [0] * 10

    while num > 0:
        counts[num % 10] += 1
        num //= 10

    ones = 0
    multiple = 0

    for e in counts:
        if e == 1:
            ones += 1
        elif e != 0:
            multiple += 1

    return ones, multiple


def pretty_sort(arr):
    nums = [None] * len(arr)

    for i in range(len(arr)):
        nums[i] = convert(arr[i])

    count_sort(nums, arr, 1, False)
    count_sort(nums, arr, 0, True)
    return arr


if __name__ == "__main__":
    arr = pretty_sort([114577, 2344, 123, 67333, 1266, 455])
    print(arr)
