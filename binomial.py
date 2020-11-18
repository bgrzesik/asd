


def binomial_iter(n):

    last = 1

    for k in range(n + 1):
        yield last
            
        last *= (n - k)
        last /= (k + 1)


if __name__ == "__main__":
    print("2 =>")
    for b in binomial_iter(2):
        print(b)
    print("\n\n3 =>")
    for b in binomial_iter(3):
        print(b)
    print("\n\n4 =>")
    for b in binomial_iter(4):
        print(b)
