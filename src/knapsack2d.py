def knapsack2d(V, max_w, max_h):
    tab = [[0] * (max_h + 1) for _ in range(max_w + 1)]

    for w in range(1, max_w + 1):
        for h in range(1, max_h + 1):
            for item_v, item_w, item_h in V:
                if item_w <= w and item_h <= h:
                    tab[w][h] = max(tab[w][h], tab[w - item_w][h - item_h] + item_v)

    return tab[max_w][max_h]


if __name__ == '__main__':
    P = [(5, 10, 3), (7, 8, 12), (2, 7, 3)]
    print(knapsack2d(P, 16, 15))  # wypisze 9
