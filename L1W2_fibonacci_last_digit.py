# Uses python3
# Last Digit of a Large Fibonacci Number
# Input: n
# Output: the last digit of the nth Fibonacci number

# Example: F_3 = 2
# Input: 3
# Output: 2

# Example: F331 = ....469
# Input: 331
# Output: 9

# Example:
# Input: 327305
# Output: 5

# Solution Methods:
# Use the property of the sum of two numbers


def get_fibonacci_last_digit_naive(n):
    # This is slower because we still need to store and compute large numbers.
    if n <= 1:
        return n

    previous = 0
    current = 1
    for i in range(n-1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_naive_fast(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    for i in range(n-1):
        previous, current = current % 10, (previous + current) % 10

    return current % 10


n = int(input())
out_put = get_fibonacci_last_digit_naive_fast(n)
print(out_put)

