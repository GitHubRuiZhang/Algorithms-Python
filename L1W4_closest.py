# Uses python3
# Find the closest pair of points
# Input:
# number of points: integer n
# n lines: pint i: [x_i, y_i]
# Output:
# the minimum distance

# Example:
# Input:
# 2
# 0 0
# 3 4
# Output:
# 5.0
# Explanation:
# distance between (0,0) and (3,4)

# Example:
# Input:
# 4
# 7 7
# 1 100
# 4 8
# 7 7
# Output:
# 0.0
# Explanation:
# distance between (7,7) and (7,7)

# Example:
# Input:
# 11
# 4 4
# -2 -2
# -3 -4
# -1 3
# 2 3
# -4 0
# 1 1
# -1 -1
# 3 -1
# -4 2
# -2 4
# Output:
# 1.414213
# Explanation:
# distance between (-1,-1) and (-2,-2); or (-2,4) and (-1,3)

# Solution Methods:
# divide-and conquer
# divide the set of points S into two subsets S1 and S2
# combine the solutions of two subsets
# notice that the distance between a point in S1 and a point in S2 can be smaller than the solution


import random


def distance(x, y):
    return ((x[0]-y[0])**2.0 + (x[1]-y[1])**2.0)**0.5


def partition2(a, l, r, xy):
    x = a[l][xy]
    y = a[l][1 - xy]
    j = l
    for i in range(l + 1, r + 1):
        if a[i][xy] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
        if a[i][xy] == x:
            if a[i][1 - xy] < y:
                j += 1
                a[i], a[j] = a[j], a[i]

    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r, xy):
    if l >= r:
        return a
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m = partition2(a, l, r, xy)
    randomized_quick_sort(a, l, m - 1, xy)
    randomized_quick_sort(a, m + 1, r, xy)

    return a


def minimum_distance_with_sort(data):
    n = len(data)
    # simple cases
    if n == 1:
        return float("inf")
    if n == 2:
        return distance(data[0], data[1])
    if n == 3:
        return min(distance(data[0], data[1]), distance(data[0], data[2]), distance(data[1], data[2]))

    # divide and conquer
    mid = n // 2
    min_left = minimum_distance_with_sort(data[:mid])
    min_right = minimum_distance_with_sort(data[mid:])
    min_lr = min(min_left, min_right)

    if min_lr == 0:
        return 0

    # special cases
    for i in range(mid):
        ch_x = data[mid - i - 1][1]
        ch_y = data[mid - i - 1][0]
        if abs(ch_x - data[mid][1]) < min_lr:
            min_lr = min(min_lr, distance(data[mid - i - 1], data[mid]))
            if min_lr == 0:
                return 0
        else:
            break

        for j in range(1, n - mid):
            if abs(ch_x - data[mid + j][1]) >= min_lr:
                break
            else:
                if abs(ch_y - data[mid + j][0]) < min_lr:
                    min_lr = min(min_lr, distance(data[mid - i - 1], data[mid + j]))
                    if min_lr == 0:
                        return 0
                else:
                    break

    return min_lr


n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

data_x = randomized_quick_sort(data, 0, n - 1, 1)
print("{0:.9f}".format(minimum_distance_with_sort(data_x)))
