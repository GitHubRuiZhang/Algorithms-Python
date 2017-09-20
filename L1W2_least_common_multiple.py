# Uses python3
# Least Common Multiple
# Input: two integers a and b
# Output: their least common multiple

# Example:
# Input: 6 8
# Output: 24

# Example:
# Input: 28851538 1183019
# Output: 1933053046

# Solution Methods:
# Use: lcm(a,b)*gcd(a,b) = a*b


def lcm_fast(a, b):
    return (a*b)//gcd_fast(a, b)
    # In python3, / is float division
    # In python2, / is integer division(with int inputs)
    # In python2 and python3, // is integer division


def gcd_fast(a, b):
    # this algorithm uses Euclid's rule to find greatest common divisor
    a_in = min(a, b)
    b_in = max(a, b)

    if a_in == 0:
        return b_in
    else:
        return gcd_fast(a_in, (b_in % a_in))


data = input().split()
out_put = lcm_fast(int(data[0]), int(data[1]))
print(out_put)


