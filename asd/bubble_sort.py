def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    tab = [0, 0, 2, 3, 4, 1, 3, 3, 3, 4, 5]
    bubble_sort(tab)
    tab, list(sorted([0, 0, 2, 3, 4, 1, 3, 3, 3, 4, 5]))
