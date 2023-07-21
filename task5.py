"""
# Exercise 5 (decoding):
Write a function that takes a bytes object as input and decodes it to a string using UTF-8 encoding.
Example:
Input: b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
Output: "Hello, 世界"

# Test the function
input_bytes = b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
print(decode_to_string(input_bytes))

"""

# Solution
def decode_to_string(input_bytes):
    return input_bytes.decode('utf-8')

# Test the function
input_bytes = b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
print(decode_to_string(input_bytes))
