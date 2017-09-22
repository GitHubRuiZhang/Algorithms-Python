# Uses python3
# Set of Points, Set of Segments
# Compute the number of segments that contains the point
# Input:
# number of segments and points: integers s and p,
# s lines: segment i: [a_i, b_i]
# points: x1, ..., xp
# Output:
# number of segments contains point j: k1, ..., kp

# Example:
# Input:
# 2 3
# 0 5
# 7 10
# 1 6 11
# Output:
# 1 0 0

# Example:
# Input:
# 1 3
# -10 10
# -100 100 0
# Output:
# 0 0 1

# Example:
# Input:
# 3 2
# 0 5
# -3 2
# 7 10
# 1 6
# Output:
# 2 0

# Solution Methods:
# first sort the segments, and then find the solutions


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


def randomized_quick_sort(a, left, right):
    if left >= right:
        return
    k = random.randint(left, right)
    a[left], a[k] = a[k], a[left]
    less_than, more_than = partition3(a, left, right)
    randomized_quick_sort(a, left, less_than - 1)
    randomized_quick_sort(a, more_than + 1, right)


def binary_search(a, left, right, x):
    if left > right:
        return left, right
    mid = (left + right) // 2
    if x == a[mid]:
        return mid
    elif x > a[mid]:
        return binary_search(a, mid+1, right, x)
    else:
        return binary_search(a, left, mid-1, x)


def binary_search_start(a, left, right, x):
    if left > right:
        return right
    mid = (left + right) // 2
    if x == a[mid]:
        return binary_search_start(a, mid+1, right, x)
    elif x > a[mid]:
        return binary_search_start(a, mid+1, right, x)
    else:
        return binary_search_start(a, left, mid-1, x)


def binary_search_end(a, left, right, x):
    if left > right:
        return left
    mid = (left + right) // 2
    if x == a[mid]:
        return binary_search_end(a, left, mid-1, x)
    elif x > a[mid]:
        return binary_search_end(a, mid+1, right, x)
    else:
        return binary_search_end(a, left, mid-1, x)


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    randomized_quick_sort(starts, 0, len(starts) - 1) # sort with respect to the first element
    randomized_quick_sort(ends, 0, len(ends) - 1)     # sort with respect to the second element
    for i in range(len(points)):
        # use binary search to find the position of point i in the sorted list of segments
        # the difference between bs_start and bs_end is on the if x == a[mid]
        po_start = binary_search_start(starts, 0, len(starts) - 1, points[i])
        po_end = binary_search_end(ends, 0, len(ends) - 1, points[i])
        # num_start = po_start + 1
        # num_end = len(ends) - po_end
        # cnt[i] = num_start + num_end - len(ends)
        cnt[i] = po_start - po_end + 1
        
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


nm = list(map(int, input().split()))
assert len(nm) == 2
n = nm[0]
m = nm[1]
starts = []
ends = []
for i in range(n):
    startend = list(map(int, input().split()))
    assert len(startend) == 2
    starts.append(startend[0])
    ends.append(startend[1])

points = list(map(int, input().split()))
assert len(points) == m
cnt = fast_count_segments(starts, ends, points)
print(" ".join(str(x) for x in cnt))
