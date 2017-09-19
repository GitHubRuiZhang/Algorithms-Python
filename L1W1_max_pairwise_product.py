# python3
# Find the maximum
# INPUT
# n: number of integers
# a_i: integer i
# OUTPUT
# max a_i \times a_j where i != j

n = int(input())
a = [int(x) for x in input().split()]

result = 0
a.sort()

print(a[n-1]*a[n-2])
