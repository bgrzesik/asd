def counting_sort(arr, k):
    num = [0] * k
    buf = [None] * len(arr)

    for el in arr:
        num[el] += 1

    for i in range(1, k):
        num[i] += num[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        val = arr[i]

        num[val] -= 1
        buf[num[val]] = val

    arr[:] = buf


if __name__ == "__main__":
    tab = [0, 0, 2, 3, 4, 1, 3, 3, 3, 4, 5]
    counting_sort(tab, 6)
    print(tab, list(sorted([0, 0, 2, 3, 4, 1, 3, 3, 3, 4, 5])))
