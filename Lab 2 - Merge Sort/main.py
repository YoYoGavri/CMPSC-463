# Lab 2- CMPSC 463 Gabriel Nulman
import random


def merge(A, p, q, r):
    n1 = q - p
    n2 = r - q

    L = A[p:q]
    R = A[q:r]

    i = 0
    j = 0

    for index in range(p, r):
        if j >= n2 or (i < n1 and L[i] <= R[j]):
            A[index] = L[i]
            i += 1
        else:
            A[index] = R[j]
            j += 1


def merge_sort(A, p, r):
    if r - p > 1:
        q = (p + r) // 2

        merge_sort(A, p, q)
        merge_sort(A, q, r)
        merge(A, p, q, r)


if __name__ == '__main__':
    print('******Merge Sort******')
    lst = [random.randint(0, 10) for _ in range(10)]
    print('Given array is: ', lst)
    merge_sort(lst, 0, 10)
    print('Sorted array is: ', lst)

