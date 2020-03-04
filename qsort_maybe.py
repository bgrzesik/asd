from timeit import default_timer as timer


def qsort(a):

    def _part(arr, left, right):
        if right < left:
            return

        # mid = (right + left) // 2
        # if arr[left] <= arr[mid] <= arr[right]:
        #     arr[mid], arr[right] = arr[right], arr[mid]
        # elif arr[mid] <= arr[left] <= arr[right]:
        #     arr[left], arr[right] = arr[right], arr[left]

        # [-1, 1, 3, 21, 33, 42, 44, 1102]
        # 726879.9999998743
        # [-1, 1, 3, 21, 33, 42, 44, 1102]
        # 540760.00000014

        pivot = arr[right]

        slow = left - 1

        for fast in range(left, right):
            if arr[fast] <= pivot:
                slow = slow + 1
                arr[fast], arr[slow] = arr[slow], arr[fast]

        arr[slow + 1], arr[right] = arr[right], arr[slow + 1]

        return slow + 1

    def _qsort(arr, left, right):
        if right < left:
            return

        pivot = _part(arr, left, right)
        _qsort(arr, left, pivot - 1)
        _qsort(arr, pivot + 1, right)

    _qsort(a, 0, len(a) - 1)
    return a

start = timer()
arr = qsort([1102, 33, 3, -1, 21, 1, 44, 42])
end = timer()
print(arr, (end - start) * 10 ** 10)
