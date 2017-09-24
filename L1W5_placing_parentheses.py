# Uses python3
# add parentheses to a given arithmetic expression to maximize its value
# Input: string s
# Output: maximum value

# Example:
# Input:
# 1 + 5
# Output:
# 6

# Example:
# Input:
# 5 - 8 + 7 * 4 - 8 + 9
# Output:
# 200
# Explanation:
# 200 = (5-((8+7)*(4-(8+9))))

# Solution Methods:
# dynamic programming


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def min_and_max(i, j, m, M, op):
    min_value = float('inf')
    max_value = - float('inf')
    for k in range(i, j):
        a = evalt(M[i][k], M[k + 1][j], op[k - 1])
        b = evalt(M[i][k], m[k + 1][j], op[k - 1])
        c = evalt(m[i][k], M[k + 1][j], op[k - 1])
        d = evalt(m[i][k], m[k + 1][j], op[k - 1])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)

    return min_value, max_value


def get_maximum_value(dataset):
    n = int((len(dataset) + 1) // 2)

    # numbers
    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    M = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        m[i][i] = int(dataset[2 * i - 2])
        M[i][i] = int(dataset[2 * i - 2])

    # operations
    op = ['0' for i in range(n - 1)]
    for i in range(0, n - 1):
        op[i] = dataset[2 * i + 1]

    # m : min
    # M : Max
    for s in range(1, n):
        for i in range(1, n - s + 1):
            j = i + s
            m[i][j], M[i][j] = min_and_max(i, j, m, M, op)

    return M[1][n]


print(get_maximum_value(input()))
