# merge 2 adjacent slices from array a:
# a[p:q] and a[q:r]
def merge(a, p, q, r):
    n1 = q - p
    n2 = r - q
    left = a[p : q]
    right = a[q : r]
    i, j = 0, 0
    for k in range(p, r):
        if j >= n2 or (i < n1 and left[i] <= right[j]):
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1

def merge_sort(a, p, r):
    if r - p > 1:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q, r)
        merge(a, p, q, r)

if __name__ == '__main__':
    size = 100
    s = [random.randint(0, size) for _ in range(size)]
    print(s)
    merge_sort(s, 0, size)
    print(s)