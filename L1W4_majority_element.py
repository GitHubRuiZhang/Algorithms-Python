# Uses python3
# Divide-and-conquer
# Input:
# integer n,
# sequence a_0, a_1, ...,a_{n-1}
# Output:
# 1 if it contains an element that appears strictly more than n/2 times,
# and 0 otherwise

# Example:
# Input:
# 5
# 2 3 9 2 2
# Output:
# 1

# Example:
# Input:
# 4
# 1 2 3 4
# Output:
# 0

# Example:
# Input:
# 4
# 1 2 3 1
# Output:
# 0

# Solution Methods:
# Divide-and-conquer,
# If a sequence of length n contains a majority element,
# then the same element is also a majority element of one of its halves


def get_majority_element(a, left, right):
    if left == right:
        return False
    if left + 1 == right:
        return a[left]
            
    mid = (left + right) // 2
    result_left = get_majority_element(a, left, mid)
    result_right = get_majority_element(a, mid, right)
    count_left = 0
    count_right = 0
    for i in range(left, right):
        if a[i] == result_left:
            count_left += 1

    if count_left > (right - left) // 2:
        return result_left
            
    for i in range(left, right):
        if a[i] == result_right:
            count_right += 1

    if count_right > (right - left) // 2:
        return result_right
   
    return False


n = int(input())
list_n = [int(x) for x in input().split()] 
if get_majority_element(list_n, 0, n):
    print(1)
else:
    print(0)

