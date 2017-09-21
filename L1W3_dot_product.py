# Uses python3
# Maximizing Revenue in Online Ad Placement
# Input:
# integer n
# integers a1, a2, a3, ..., an
# integers b1, b2, b3, ..., bn
# Output: maximum value \sum\limits_{i=1}^n a_ic_i,
# where c1, c2, ..., cn is a permutation of b1, b2, ..., bn

# Example:
# Input:
# 1
# 23
# 39
# Output:
# 897
# Explanation: 897 = 23*39

# Example:
# Input:
# 3
# 1 3 -5
# -2 4 1
# Output: 23
# Explanation: 23 = 3*4 + 1* 1 +  (-5)*(-2)

# Solution Methods:
# Greedy Algorithm, pick maximum a_ic_i first


def max_dot_product(a, b):
    res = 0
    #sort
    a = list(sorted(a, reverse=True))
    b = list(sorted(b, reverse=True))
    #sum
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


n = input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(max_dot_product(a, b))
