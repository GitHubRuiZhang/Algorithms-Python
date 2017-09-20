# Uses python3
# Partial Sum of Fibonacci Numbers
# Input: integers m and n
# Output: last digit of f(m) + f(m+1) + ... + f(n)

# Example:
# Input: 3 7
# Output: 1

# Example:
# Input: 10 10
# Output: 5

# Example:
# Input: 10 200
# Output: 2

# Solution Methods:
# Pisano Period
# The sequence of final digits in Fibonacci numbers repeats in cycles of 60.
# See http://mathworld.wolfram.com/FibonacciNumber.html


def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to

    previous = 0
    current  = 1

    for _ in range(from_ - 1):
        previous, current = current, previous + current

    sum = current

    for _ in range(to - from_):
        previous, current = current, previous + current
        sum += current

    return sum % 10
    
    
def fibonacci_partial_sum_fast(m, n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    last_digit_all = list(range(60))

    # Get Pisano Period
    for i in range(60):
        last_digit_all[i] = previous % 10
        previous, current = current % 10, (previous + current) % 10

    # Last digit of f(0) + ... + f(n)
    numb = (n+2) % 60
    if last_digit_all[numb] == 0:
        last_digit_n = 9
    else:
        last_digit_n = last_digit_all[numb] - 1

    # Last digit of f(0) + ... + f(m-1)
    numb_m = (m+2-1) % 60
    if last_digit_all[numb_m] == 0:
        last_digit_m = 9
    else:
        last_digit_m = last_digit_all[numb_m] - 1

    # Last digit of f(m) + ... + f(n)
    return last_digit_n - last_digit_m


def get_fibonacci_last_digit_fast(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    count_i = list(range(60))
    last_digit_all = list(range(60))

    for i in count_i:
        last_digit_all[i] = previous % 10
        previous, current = current % 10, (previous + current) % 10
        
    numb = ((n) % 60 ) 
    if (last_digit_all[numb] ) == 0:
        return 9
    else:
        return last_digit_all[numb]


data = input().split()
a = int(data[0])
b = int(data[1])
if a == b:
    out_put = get_fibonacci_last_digit_fast(a)
else:
    out_put = fibonacci_partial_sum_fast(a, b)

if out_put < 0:
    out_put = 10 + out_put     

print(out_put)

