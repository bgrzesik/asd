def find_distinct(arr):
    left = 0
    right = len(arr) - 1

    count = 0

    while left <= right:
        val = max(abs(arr[left]), abs(arr[right]))
        print(val)
        count += 1
        while left <= right and abs(arr[left]) == val:
            left += 1

        while left <= right and abs(arr[right]) == val:
            right -= 1

    return count


if __name__ == "__main__":
    print("-", find_distinct([-1, -1, 0, 0, 1, 1, 1]))
    print("-", find_distinct([1, 1, 1]))
    print("-", find_distinct([-2, -1, -1, -1, 0, 0, 1, 1, 2, 3]))
    print("-", find_distinct([-5, -3, 0, 2, 3, 5, 7]))
