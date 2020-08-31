from graph_util import adj_to_dot
import math


class FastListNode:
    def __init__(self, a):
        self.a = a
        self.next = []

    def __str__(self):
        res = "a: " + str(self.a) + "\t" + "next keys: "
        res += str([n.a for n in self.next])
        return res


def fast_list_append(L: FastListNode, a: int):
    # O(log(n))

    new = FastListNode(a)

    # next = [i + 1, i + 2, i + 4, i + 8, i + 16]
    # 1                      = 1
    # 1 + 1                  = 2
    # 1 + 1 + 2              = 4
    # 1 + 1 + 2 + 4          = 8
    # 1 + 1 + 2 + 4 + 8      = 16
    # 1 + 1 + 2 + 4 + 8 + 16 = 32

    i = L
    idx = 0
    while i is not None:
        new.next.append(i)
        i = i.next[idx] if idx < len(i.next) else None
        idx += 1

    return new


if __name__ == "__main__":
    L = FastListNode(119)
    for e in [107, 103, 21, 12, 9, 4, 3, 2, 1]:
        L = fast_list_append(L, e)

    i = 0
    while L is not None:
        print(f"{L.a} [label=\"{i}: {L.a}\"]")
        print("\n".join([f"{L.a} -> {l.a}" for l in L.next]))

        i += 1
        L = L.next[0] if len(L.next) != 0 else None
