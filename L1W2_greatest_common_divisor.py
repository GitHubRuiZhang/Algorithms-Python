# Uses python3
# Greatest common divisor
# Input: two integers a and b
# Output: their greatest common divisor

# Example:
# Input: 18 35
# Output: 1

# Example:
# Input: 28851538 1183019
# Output: 17657

# Solution Methods:
# Use Euclid's rule: gcd(x,y) = gcd(x mod y,y)


def gcd_naive(a, b):
    # this algorithm iterates from 2 to min(a,b) to find the gcd
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_fast(a, b):
    # this algorithm uses Euclid's rule
    a_in = min(a, b)
    b_in = max(a, b)
    
    if a_in == 0:
        return b_in
    else:
        return gcd_fast(a_in, (b_in % a_in))
        

data = input().split()
out_put = gcd_fast(int(data[0]),int(data[1]))
print(out_put)
