# Uses python3
# Binary search
# Input:
# integer n, sequence a_0 < a_1 < ... < a_{n-1}
# integer k, sequence b_0, b_1, ..., b_{k-1}
# Output:
# sequence of size k, i.e., c_0, c_1, ..., c_{k-1}
# where a_{c_j} = b_j

# Example:
# Input:
# 5 1 5 8 12 13
# 5 8 1 23 1 11
# Output:
# 2 0 -1 0 -1

# Solution Methods:
# Binary search


def binary_search(a, left, right, x):
    if left > right:
        return -1
    mid = (left + right) // 2
    if x == a[mid]:
        return mid
    elif x > a[mid]:
        return binary_search(a, mid+1, right, x)
    else:
        return binary_search(a, left, mid-1, x)
          

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


dic_in = [int(x) for x in input().split()] 
look_in = [int(x) for x in input().split()] 
n = dic_in[0]
m = look_in[0]
dic = dic_in[1:]
look = look_in[1:]
out_put = []
for i in range(len(look)):
    out_put.append(binary_search(dic, 0, n-1, look[i]))

print(' '.join(str(it) for it in out_put))
