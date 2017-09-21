# Uses python3
# Maximizing the Number of Prize Places in a Competition
# Input: integer n
# Output:
# line 1: the maximum number k such that n can be represented as a sum
# of k pairwise distinct positive integers
# line 2: k pairwise distinct positive integers that sum up to n

# Example:
# Input: 6
# Output:
# 3
# 1 2 3
# Explanation: 6 = 1 + 2 + 3

# Example:
# Input: 8
# Output:
# 3
# 1 2 5
# Explanation: 8 = 1 + 2 + 5

# Solution Methods:
# Greedy Algorithm, pick 1, then pick 2, ..., remember we cannot pick 1,2... again
# Start with 1, 2, 3, ...
# Given integers k and l, where l <= k, we pick the summand using the following method:
# if k <= 2l, we pick k, otherwise, we pick l.


def optimal_summands(n):
    summands = []  
    k = n
    l = 1  
    while True:
        if k <= 2*l:
            summands.append(k)
            break 
        else:
            summands.append(l)
            k -= l
            l += 1
    return summands


summands = optimal_summands(int(input()))
print(len(summands))
print(' '.join(str(it) for it in summands))
