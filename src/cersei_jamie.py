def cersei_jamie(activites):
    parents = ["*"] * len(activites)
    times = []
    idx = 0
    for start, stop in activites:
        times.append((start, idx, True))
        times.append((stop, idx, False))
        idx += 1

    times.sort(key=lambda a: a[0])

    jamie = False
    cersei = False

    for time, ac, start in times:
        if start:
            if jamie is False:
                jamie = True
                parents[ac] = "J"
            elif cersei is False:
                cersei = True
                parents[ac] = "C"
            else:
                print("IMPOSIBRU")
                break
        else:
            if parents[ac] == "J":
                jamie = False
            elif parents[ac] == "C":
                cersei = False

    print("".join(parents))


if __name__ == '__main__':
    cersei_jamie([(99, 150), (1, 100), (100, 301), (2, 5), (150, 250)])
