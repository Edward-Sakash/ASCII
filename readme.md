# Exercise 1 (ASCII):
Write a function that takes a string as input and returns its corresponding ASCII representation as a list of integers.

Example:
Input: "Hello"
Output: [72, 101, 108, 108, 111]
# Test the function
input_str = "Hello"
print(string_to_ascii(input_str))

# Exercise 2 (Decimal - Binary):
Write a function that takes an integer as input and returns its binary representation as a string.
Input: 42
Output: "101010"

# Test the function
input_int = 42
print(int_to_binary(input_int))

# Exercise 3 (Hexadecimal - decimal):
Write a function that takes a hexadecimal string as input and returns its decimal (integer) value.
Example:
Input: "1A"
Output: 26

# Test the function
hex_str = "1A"
print(hex_to_int(hex_str))

# Exercise 4 (encoding):
Write a function that takes a string and encodes it to bytes using UTF-8 encoding.
Input: "Hello, 世界"
Output: b'Hello, \xe4\xb8\x96\xe7\x95\x8c'

# Test the function
input_str = "Hello, 世界"
print(encode_to_bytes(input_str))

# Exercise 5 (decoding):
Write a function that takes a bytes object as input and decodes it to a string using UTF-8 encoding.
Example:
Input: b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
Output: "Hello, 世界"

# Test the function
input_bytes = b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
print(decode_to_string(input_bytes))