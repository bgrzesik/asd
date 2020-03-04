from math import floor, ceil
from timeit import default_timer as timer


def find(tab, el):
    left = 0
    right = len(tab) - 1

    while left <= right:
        mid = (left + right) // 2

        if el == tab[mid]:
            return mid
        elif el > tab[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def find2(tab, el):
    for i in range(len(tab)):
        if tab[i] == el:
            return i

    return -1


def find3(tab, el):
    left = 0
    right = len(tab) - 1

    while left < right:
        range_size = right - left

        part1 = left + range_size // 4 + 1
        part2 = right - range_size // 4

        # print(left, part1, part2, right)

        if tab[part1] > el:
            right = part1
        elif tab[part1] < el < tab[part2]:
            left = part1
            right = part2
        elif tab[part2] < el:
            left = part2
        elif tab[part1] == el:
            return part1
        elif tab[part2] == el:
            return part2
        else:
            raise RuntimeError("Co do wafla?")

        if range_size < 4:
            return -1

    return -1


def find4(tab, el):
    left = 0
    right = len(tab) - 1

    if not tab[left] <= el <= tab[right]:
        return -1

    while left <= right:
        mid = int((el - tab[left]) * (right - left) / (tab[right] - tab[left]))

        if el == tab[mid]:
            return mid
        elif el > tab[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    test_data = list(range(2013))

    start = timer()
    assert find(test_data, 10) == 10
    assert find(test_data, 50) == 50
    assert find(test_data, 702) == 702
    assert find(test_data, 2012) == 2012
    assert find(test_data, 201200) == -1
    end = timer()

    print("find {}".format((end - start) *
                           (10 ** 7)))

    start = timer()
    assert find2(test_data, 10) == 10
    assert find2(test_data, 50) == 50
    assert find2(test_data, 2012) == 2012
    assert find2(test_data, 201200) == -1
    end = timer()

    print("find2 {}".format((end - start) * (10 ** 7)))

    start = timer()
    assert find3(test_data, 10) == 10
    assert find3(test_data, 50) == 50
    assert find3(test_data, 2012) == 2012
    assert find3(test_data, 201200) == -1
    end = timer()

    print("find3 {}".format((end - start) * (10 ** 7)))

    start = timer()
    assert find4(test_data, 10) == 10
    assert find4(test_data, 50) == 50
    assert find4(test_data, 2012) == 2012
    assert find4(test_data, 201200) == -1
    end = timer()

    print("find4 {}".format((end - start) * (10 ** 7)))
