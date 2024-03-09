# Python program to implement an Optimized
# Solution to check Deficient Number
import math


# Function to calculate sum of divisors
def divisors_sum(n):
    sum = 0  # Initialize sum of prime factors

    # Note that this loop runs till square
    # root of n
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:

            # If divisors are equal, take only one
            # of them
            if n / i == i:
                sum = sum + i
            else:  # Otherwise take both
                sum = sum + i
                sum = sum + (n / i)
        i = i + 1
    return sum


# Function to check Deficient Number
def is_deficient(n):
    # Check if sum(n) < 2 * n
    if divisors_sum(n) < (2 * n):
        return True
    else:
        return False


print(is_deficient(4))
