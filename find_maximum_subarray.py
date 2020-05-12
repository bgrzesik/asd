
def _find_max_subarr_crossing(A, low, mid, high):
    max_left = float("-inf")
    left_end = mid
    left = 0

    for i in range(mid, low - 1, -1):
        left += A[i]
        if max_left < left:
            max_left = left
            left_end = i

    max_right = float("-inf")
    right_end = mid
    right = 0

    for i in range(mid + 1, high + 1):
        right += A[i]
        if max_right < right:
            max_right = right
            right_end = i

    return left_end, right_end, (max_left + max_right)


def find_maximum_subarray(A, low=None, high=None):
    low = low if low is not None else 0
    high = high if high is not None else (len(A) - 1)

    if low >= high:
        return low, high, A[low]

    mid = (low + high) // 2

    left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
    right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)
    mid_low, mid_high, mid_sum = _find_max_subarr_crossing(A, low, mid, high)

    if left_sum > right_sum and left_sum > mid_sum:
        return left_low, left_high, left_sum
    elif right_sum > mid_sum and right_sum > mid_sum:
        return right_low, right_high, right_sum
    else:
        return mid_low, mid_high, mid_sum


if __name__ == "__main__":
    assert  find_maximum_subarray([1, -4, 3, 4, -4]) == (2, 3, 7)