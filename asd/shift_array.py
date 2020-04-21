

def shift_array(arr, n):
    def reverse(arr, start, stop):
        for _ in range((stop - start) // 2):
            arr[start], arr[stop] =  arr[stop], arr[start]
            start += 1
            stop -= 1

    reverse(arr, len(arr) - n, len(arr) - 1)
    reverse(arr, 0, len(arr) - 1 - n)
    reverse(arr, 0, len(arr) - 1)

    return arr


if __name__ == "__main__":
    print(shift_array([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))
