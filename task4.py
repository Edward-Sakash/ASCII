"""
# Exercise 4 (encoding):
Write a function that takes a string and encodes it to bytes using UTF-8 encoding.
Input: "Hello, 世界"
Output: b'Hello, \xe4\xb8\x96\xe7\x95\x8c'

# Test the function
input_str = "Hello, 世界"
print(encode_to_bytes(input_str))

"""

# Solution
def encode_to_bytes(input_str):
    return input_str.encode('utf-8')

# Test the function
input_str = "Hello, 世界"
print(encode_to_bytes(input_str))
