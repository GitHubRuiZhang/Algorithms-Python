# Uses python3
# Knapsack without repetitions
# Input:
# capacity: integer W; number of bars of gold: n
# weights: w1,...,wn
# Output: maximum weight of gold that fits into a knapsack of capacity W

# Example:
# Input:
# 10 3
# 1 4 8
# Output:
# 9
# Explanation:
# 1 + 8 = 9

# Solution Methods:
# dynamic programming


def optimal_weight(W, w):
    weight_list = [[0 for _ in range(W + 1)] for _ in range(len(w) + 1)]
    for j in range(1, W + 1):
        for i in range(1, len(w) + 1):
            # not_used_val
            weight_list[i][j] = weight_list[i - 1][j]
            if j >= w[i - 1]:
                used_val = weight_list[i - 1][j - w[i - 1]] + w[i - 1]
                if used_val > weight_list[i - 1][j]:
                    weight_list[i][j] = used_val

    return weight_list[len(w)][W]


number_capacity = [int(x) for x in input().split()]
Capacity = int(number_capacity[0])
Number = int(number_capacity[1])
w = [int(x) for x in input().split()]
print(optimal_weight(Capacity, w))
