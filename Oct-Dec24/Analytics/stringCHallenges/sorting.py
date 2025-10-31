import random

from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

lst = []
for _ in range(0, 12):
    lst.append(random.randint(1, 100))

lst.sort()

def find(lst, val):
    for elm in lst:
        if elm == val:
            return True
    return False



def find_index(lst, val):
    for i in range(0, len(lst)):
        if lst[i] == val:
            return i
    return -1


## linear, runs once for every item in list. f(x)=x, O(n)
## BC, Avg C, WC (Worst case most important)
## O(1), O(n), O(n)

## bubble sort
## BC, AC, WC
## O(n^2)



def find_binary(lst, val):
    low = 0
    high = len(lst) - 1
    print(low, high)
    while low <= high:
        mid = (low + high)//2
        print(low, mid, high)

        if lst[mid] == val:
            return mid
        elif lst[mid] > val:
            high = mid - 1
        elif lst[mid] < val:
            low = mid + 1

    print(low, mid, high)

    if lst[low] == val:
        return low
    else:
        return -1


## binary search
## WC
## O(log n)

## quick sort
## BC/AC        WC
## O(n log n)   O(n^2)

print(find_binary(lst, 25))

print(find(lst, 25))
print(find_index(lst, 25))
print(lst)