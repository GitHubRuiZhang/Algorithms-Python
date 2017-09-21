# Uses python3
# Maximizing the Value of a Loot
# Input:
# the number of items n and the capacity of a knapsack W
# n lines: values and weights of the items v_i and w_i
# Output: maximal value of fractions of items that fit into the knapsack

# Example:
# Input:
# 3 50
# 60 20
# 100 50
# 120 30
# Output:
# 180.00
# Explanation: 60 20 + 120 30

# Example:
# Input:
# 1 10
# 500 30
# Output: 166.6667
# Explanation: One third of the only available item

# Solution Methods:
# Greedy Algorithm, Knapsack Problem


def get_optimal_value(capacity, weights, values):
    value = 0.0
    # sort the list, large to small
    if len(weights) != len(values):
            return False
    item_individual = [0] * len(weights)    
    for i in range(len(weights)):
        # value/weight
        item_individual[i] = values[i] / weights[i] 

    # sort, but we need the index
    item_index = list(sorted(range(len(item_individual)), key=item_individual.__getitem__,reverse=True))
    # get the sorted order of weights and values
    weights = [weights[i] for i in item_index]
    values = [values[i] for i in item_index]
    # fill the bag using greedy algorithm
    for i in range(len(weights)):
        if capacity == 0:
            break
        if weights[i] <= capacity:
            value += values[i]
            capacity -= weights[i]           
        else:
            value += capacity * values[i] / float(weights[i])
            capacity = 0
    
    return round(value, 4)


Number_Capacity = input().split()
Number = int(Number_Capacity[0])
Capacity = int(Number_Capacity[1])

Item_Values = [0] * Number
Item_Weight = [0] * Number
for i in range(Number):
    Item = input().split()
    Item_Values[i] = int(Item[0])
    Item_Weight[i] = int(Item[1])

print(get_optimal_value(Capacity, Item_Weight, Item_Values))