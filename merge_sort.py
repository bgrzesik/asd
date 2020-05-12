
def merge(A, p, q, r):
    L = A[p:q + 1].copy()
    R = A[q + 1:r + 1].copy()

    B = []

    i = 0
    j = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            B.append(L[i])
            i += 1
        else:
            B.append(R[j])
            j += 1

    A[p:r+1] = B + L[i:] + R[j:]


def merge_sort(arr, p=0, k=None):
    if k is None:
        k = len(arr) - 1

    if p == k:
        return

    sr = (p + k) // 2

    merge_sort(arr, p, sr)
    merge_sort(arr, sr + 1, k)
    merge(arr, p, sr, k)


if __name__ == "__main__":
    tab = [1, 2, -2, 1, 4, 10, 11, 1, 405]
    merge_sort(tab)
    print(tab)