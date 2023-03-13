lst = [12, 14, -3, 57, 96, 437, 84, 46, 63, 8]


def insertion_sort(lst):
    for j in range(0, len(lst)):
        key = lst[j]
        i = j - 1
        while i >= 0 and lst[i] > key:
            lst[i + 1] = lst[i]
            i -= 1
        lst[i + 1] = key
    return lst


print(f'The unsorted list is: {lst}')
print(f'The sorted list is: {insertion_sort(lst)}')
