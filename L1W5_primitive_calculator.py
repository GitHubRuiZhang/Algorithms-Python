# Uses python3
# Primitive calculator
# Achieve n by operations: multiply 2, multiply 3, or add 1
# Input: integer n
# Output:
# minimum number of operations
# intermediate numbers

# Example:
# Input:1
# Output:
# 0
# 1
# Explanation:
# 1

# Example:
# Input: 5
# Output:
# 3
# 1 2 4 5
# Explanation:
# 1 * 2 = 2, 2 * 2 = 4, 4 + 1 = 5

# Example:
# Input: 14
# Output:
# 14
# 1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
# or
# 1 3 9 10 11 33 99 297 891 2673 8019 16038 16039 48117 96234

# Solution Methods:
# dynamic programming
# primitive_calculator(n)=min(primitive_calculator(n//2),primitive_calculator(n//3),or primitive_calculator(n-1))+1


def find_operation(n):
    if n == 1:
        return [1]

    num = [0] * (n + 1)

    for i in range(1, n + 1):
        # simple cases
        if i == 1:
            num[i] = 0
            continue
        if i == 2:
            num[i] = 1
            continue
        if i == 3:
            num[i] = 1
            continue

        # divide totally?
        if i % 2 == 0:
            num[i] = min(num[i - 1], num[int(i // 2)]) + 1
        if i % 3 == 0:
            num[i] = min(num[i - 1], num[int(i // 3)]) + 1
        if not (i % 2 == 0 or i % 3 == 0):
            num[i] = num[i - 1] + 1

    # find the intermediate numbers
    detail = [n]
    i = n
    while True:
        if i == 1:
            break
        if i == 2:
            detail.append(1)
            break
        if i == 3:
            detail.append(1)
            break

        if i % 2 == 0:
            if num[i] == num[int(i // 2)] + 1:
                detail.append(int(i // 2))
                i = i // 2
                continue
        if i % 3 == 0:
            if num[i] == num[int(i // 3)] + 1:
                detail.append(int(i // 3))
                i = i // 3
                continue
        if num[i] == num[i - 1] + 1:
            detail.append(i - 1)
            i -= 1

    return detail[::-1]


n = int(input())
out_put = find_operation(n)
print(len(out_put) - 1)
print(' '.join(str(it) for it in out_put))
