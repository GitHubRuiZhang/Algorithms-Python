# Uses python3
# Small Fibonacci Number
# Input: n
# output: nth Fibonacci number

# Example:
# Input: 3
# Output: 2

# Example:
# Input: 10
# Output: 55


def calc_fib(n):
    f_all = []
    for i in range(n):
        if i <= 1:
            f_all.append(i)
        else:
            f_all.append(f_all[-1]+f_all[-2])
    return f_all[-1]


n = int(input())
print(calc_fib(n+1))
