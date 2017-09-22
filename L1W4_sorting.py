# Uses python3
# 3-way partition sort
# Input:
# integer n,
# sequence a_0, a_1, ...,a_{n-1}
# Output:
# sequence sorted in non-decreasing order

# Example:
# Input:
# 5
# 2 3 9 2 2
# Output:
# 2 2 2 3 9

# Solution Methods:
# change the 2-way partition sort into 3-way partition sort


import random


def partition3(a, l, r):
    x = a[l]
    m = l
    n = r
    i = l
    while i <= n:       
        if a[i] > x:
            a[i], a[n] = a[n], a[i]
            n -= 1
            i -= 1 
        elif a[i] < x:           
            a[i], a[m] = a[m], a[i]
            m += 1       
        i += 1
    
    return m, n


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, left, right):
    if left >= right:
        return
    k = random.randint(left, right)
    a[left], a[k] = a[k], a[left]
    less_than, more_than = partition3(a, left, right)
    randomized_quick_sort(a, left, less_than-1)
    randomized_quick_sort(a, more_than+1, right)


n = int(input())
list_n = [int(x) for x in input().split()] 
randomized_quick_sort(list_n, 0, n - 1)
print(' '.join(str(it) for it in list_n))
