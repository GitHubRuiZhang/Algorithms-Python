# Uses python3
# Huge Fibonacci Number modulo m
# Input: two integers n and m
# Output: Fibonacci number f(n) mod m

# Example:
# Input: 1 239
# Output: 1

# Example:
# Input: 239 1000
# Output: 161

# Example:
# Input: 28851538 1183019
# Output: 1933053046

# Solution Methods:
# The output will repeat, Pisano period
# i         0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# f         0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610
# f mod 2   0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0
# f mod 3   0 1 1 2 0 2 2 1 0 1 1 2 0 2 2 1


def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1
    digit_period = []
    for i in range(n + 1):
        digit_period.append(previous % m)
        previous, current = current % m, (previous + current) % m
        if i >= 3:
            if (previous == 0) and (current == 1):
                return digit_period[n % len(digit_period)]
                break

    # this is used to guarantee that we always have an output
    return digit_period[n]


data = input().split()
out_put = get_fibonacci_huge(int(data[0]), int(data[1]))
print(out_put)
