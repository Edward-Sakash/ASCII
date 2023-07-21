"""
# Exercise 1 (ASCII):
Write a function that takes a string as input and returns its corresponding ASCII representation as a list of integers.

Example:
Input: "Hello"
Output: [72, 101, 108, 108, 111]
# Test the function
input_str = "Hello"
print(string_to_ascii(input_str))

"""
# Solution

def string_to_ascii(input_str):
    return [ord(char) for char in input_str]

# Test the function
input_str = "Hello Edward"
print(string_to_ascii(input_str))
