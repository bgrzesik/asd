from pprint import pprint


def ferry(A, D):
    dyn = [[[None for _ in range(D + 1)]
            for _ in range(D + 1)] for _ in range(len(A))]
    lanes = [[['N' for _ in range(D + 1)]
              for _ in range(D + 1)] for _ in range(len(A))]

    for l in range(D + 1):
        for r in range(D + 1):
            if A[0] <= r:
                dyn[0][l][r] = 1
                lanes[0][l][r] = "R"
            elif A[0] <= l:
                dyn[0][l][r] = 1
                lanes[0][l][r] = "L"
            else:
                dyn[0][l][r] = 0

    for i in range(len(A)):
        dyn[i][0][0] = 0
        lanes[i][0][0] = 'N'

    def f(i, l, r):
        if dyn[i][l][r] is not None:
            return dyn[i][l][r]

        n = 0
        car = "N"

        if i != 0:
            n = f(i - 1, l, r)

        if l >= A[i]:
            fl = f(i - 1, l - A[i], r) + 1

            if n < fl:
                n = fl
                car = "L"

        if r >= A[i]:
            fr = f(i - 1, l, r - A[i]) + 1

            if n < fr:
                n = fr
                car = "R"

        dyn[i][l][r] = n
        lanes[i][l][r] = car

        return dyn[i][l][r]

    f(len(A) - 1, D, D)

    l = D
    r = D
    order = ""

    for i in range(len(A) - 1, -1, -1):
        lane = lanes[i][l][r]

        if lane == "L":
            l -= A[i]
        elif lane == "R":
            r -= A[i]

        order = lane + order

    return order


if __name__ == "__main__":
    print(ferry([1, 2, 3, 4, 5, 7], 5))
