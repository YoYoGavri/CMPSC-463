# Lab 3 - QuickSort - CMPSC 463
# Gabriel Nulman - gkn5075@psu.edu

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


lst = [2, 5, 6, 1, 4, 6, 2, 4, 7, 8, 3, 27, 9, 12]
print("Unsorted List: ", lst)

quicksort(lst, 0, len(lst) - 1)

print("Sorted List: ", lst)
