# Uses python3
# Maximizing Your Salary
# Compose the largest number out of a set of integers
# Input:
# integer n
# a1, a2, ..., an
# Output:
# the largest number that can be composed

# Example:
# Input:
# 2
# 21 2
# Output: 221

# Example:
# Input:
# 5
# 9 4 6 1 9
# Output: 99641

# Example:
# Input:
# 3
# 23 39 92
# 923923

# Solution Methods:
# Greedy Algorithm, pick the largest first


def largest_number(a):
    results = []
    while a:
        max_digit = 0
        for digit in a:
            # This is a simple method, don't over think about it
            if str(digit) + str(max_digit) > str(max_digit) + str(digit):
                max_digit = digit

        results.append(max_digit)
        a.remove(max_digit)

    return results


n = int(input())
a = [int(x) for x in input().split()]
assert (len(a) == n)
Lar_Num = largest_number(a)
print(''.join(str(it) for it in Lar_Num))
