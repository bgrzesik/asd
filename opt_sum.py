

def opt_sum(tab):

    tab.sort()

    i = 1
    j = -2

    s = tab[0] + tab[-1]
    m = abs(s)

    for _ in range(len(tab) - 2):
        if abs(s + tab[i]) < abs(s + tab[j]):
            s += tab[i]
            i += 1
        else:
            s += tab[j]
            j -= 1

        m = max(m, abs(s))

    return m
