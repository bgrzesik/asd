def insert_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]

        j = i - 1

        while i >= 0 and arr[j] > val:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = val


if __name__ == "__main__":
    tab = [0, 0, 2, 3, 4, 1, 3, 3, 3, 4, 5]
    insert_sort(tab)
    print(tab, list(sorted([0, 0, 2, 3, 4, 1, 3, 3, 3, 4, 5])))
