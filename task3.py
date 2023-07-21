"""
# Exercise 3 (Hexadecimal - decimal):
Write a function that takes a hexadecimal string as input and returns its decimal (integer) value.
Example:
Input: "1A"
Output: 26

# Test the function
hex_str = "1A"
print(hex_to_int(hex_str))    

"""
# Solution
def hex_to_int(hex_str):
    return int(hex_str, 16)

# Test the function
hex_str = "1A"
print(hex_to_int(hex_str))
