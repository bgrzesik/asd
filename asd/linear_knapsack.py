def knapsack(A, k):
    A.sort(key=lambda a: a[0] / a[1], reverse=True)

    profit = 0

    for p, w in A:
        quantity = min(k, w)

        profit += p * quantity / w

        k -= quantity

        if k <= 0:
            break;

    return profit


if __name__ == "__main__":
    print(knapsack([(1, 1), (10, 2), (6, 3)], 3))
