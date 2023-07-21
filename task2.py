"""
# Exercise 2 (Decimal - Binary):
Write a function that takes an integer as input and returns its binary representation as a string.
Input: 42
Output: "101010"

# Test the function
input_int = 42
print(int_to_binary(input_int))
    
"""

# Solution
def int_to_binary(input_int):
    binary_str = bin(input_int)[2:]
    return binary_str

# Test the function
input_int = 42
print(int_to_binary(input_int))
