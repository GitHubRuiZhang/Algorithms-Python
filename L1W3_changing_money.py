# Uses python3
# Changing Money
# Input: integers m
# Output: minimum number of coins with denominations 1, 5, 10 that changes m

# Example:
# Input: 2
# Output: 2
# Explanation: 2 = 1 + 1

# Example:
# Input: 28
# Output: 6
# Explanation: 28 = 10 + 10 + 5 + 1 + 1 + 1

# Solution Methods:
# Greedy Algorithm


def get_change(m):
    n = 0
    if (m // 10) >= 1:
        n += (m // 10) # // floor division
        m = m % 10
        
    if (m // 5) >= 1:
        n += (m // 5)
        m = m % 5
        
    n += m
    
    return n


m = int(input())
print(get_change(m))
