# Uses python3
# Last Digit of the Sum of Fibonacci Numbers
# Input: integer n
# Output: the last digit of the sum f(0) + f(1) + ... + f(n)

# Example:
# Input: 3
# Output: 4

# Example:
# Input: 100
# Output: 5


# Solution Methods:
# Pisano Period
# The sequence of final digits in Fibonacci numbers repeats in cycles of 60.
# See http://mathworld.wolfram.com/FibonacciNumber.html


def fibonacci_sum_naive(n):
    # The sum of the first n Fibonacci numbers is the (n+2)nd Fibonacci number minus 1
    if n <= 1:
        return n

    previous = 0
    current = 1
    count_i = range(n-1+2)
    for i in count_i:
        previous, current = current % 10, (previous + current) % 10

    return (current-1) % 10


def fibonacci_sum_fast(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    last_digit_all = list(range(60))

    for i in range(60):
        last_digit_all[i] = previous % 10
        previous, current = current % 10, (previous + current) % 10
        
    numb = ((n+2) % 60)
    if (last_digit_all[numb]) == 0:
        return 9
    else:
        return last_digit_all[numb] - 1

    
n = int(input())
out_put = fibonacci_sum_fast(n)
print(out_put)
