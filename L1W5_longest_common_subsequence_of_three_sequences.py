# Uses python3
# longest common subsequence of three sequences
# 1 < i1 < i2 < ... < ip < n
# 1 < j1 < j2 < ... < jp < m
# 1 < k1 < k2 < ... < kp < l
# ai1 = bj1 =ck1, ..., aip = bjp =ckp
# Input:
# n
# a1,a2,...,an
# m
# b1,b2,...,bm
# l
# c1,c2,...,cl
# Output: length of longest subsequence

# Example:
# Input:
# 3
# 1 2 3
# 3
# 2 1 3
# 3
# 1 3 5
# Output:
# 2
# Explanation:
# 1 3

# Example:
# Input:
# 5
# 8 3 2 1 7
# 7
# 8 2 1 3 8 10 7
# 6
# 6 8 3 1 4 7
# Output:
# 3
# Explanation:
# 8 3 7
# or 8 1 7

# Solution Methods:
# dynamic programming
# edit distance


def edit_distance3(s, t, u):
    D = [[[0 for k in range(len(u) + 1)] for j in range(len(t) + 1)] for i in range(len(s) + 1)]

    for k in range(1, len(u) + 1):
        for j in range(1, len(t) + 1):
            for i in range(1, len(s) + 1):
                ID4 = D[i][j - 1][k]
                ID5 = D[i - 1][j][k]
                ID6 = D[i][j][k - 1]
                Match = D[i - 1][j - 1][k - 1]
                if s[i - 1] == t[j - 1] and t[j - 1] == u[k - 1]:
                    D[i][j][k] = Match + 1
                else:
                    D[i][j][k] = max(ID4, ID5, ID6)

    Common = []
    i = len(s)
    j = len(t)
    k = len(u)
    while True:
        if i == 0 or j == 0 or k == 0:
            break

        if D[i][j][k] == D[i - 1][j][k]:
            i -= 1
        elif D[i][j][k] == D[i][j - 1][k]:
            j -= 1
        elif D[i][j][k] == D[i][j][k - 1]:
            k -= 1
        else:
            Common.append(s[i - 1])
            i -= 1
            j -= 1
            k -= 1

    return len(Common[::-1])


an = int(input())
a = [int(x) for x in input().split()]
bn = int(input())
b = [int(x) for x in input().split()]
cn = int(input())
c = [int(x) for x in input().split()]
print(edit_distance3(a, b, c))
