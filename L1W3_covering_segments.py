# Uses python3
# Collecting Signatures
# A set of segments on a line, mark as few points on a line as possible
# so that each segment contains at least one marked point
# Input:
# number of segments, integer n
# n lines: ith segment, a_i,b_i
# Output:
# minimum number of points m
# integer coordinates of m points

# Example:
# Input:
# 3
# 1 3
# 2 5
# 3 6
# Output:
# 1
# 3
# Explanation: 1<=3<=3, 2<=3<=5, 3<=3<=6

# Example:
# Input:
# 4
# 4 7
# 1 3
# 2 5
# 5 6
# Output:
# 2
# 3 6
# Explanation: 4<=3<=6<=7,1<=3<=3,2<=3<=3,5<=6<=6

# Solution Methods:
# Greedy Algorithm, pick the ends


def optimal_points(starts, ends):
    points = []
    #sort
    item_index = list(sorted(range(len(ends)), key=ends.__getitem__, reverse=False))
    starts = [starts[i] for i in item_index]
    ends = [ends[i] for i in item_index]
    #Find
    for i in range(len(ends)):
        if i == 0:
            points.append(ends[i])
        elif ends[i-1] < starts[i]:
            # no interactions between previous segment and this segment
            points.append(ends[i])      
        elif points[-1] < starts[i]:
            # last point is outside this segment
            points.append(ends[i])
        # otherwise we do not need to add points
            
    return points
        

n = int(input())
Starts = [0] * n
Ends = [0] * n
for i in range(n):
    Item = input().split()
    Starts[i] = int(Item[0])
    Ends[i] = int(Item[1])

Results = optimal_points(Starts, Ends)
print(len(Results))
print(' '.join(str(it) for it in Results))
