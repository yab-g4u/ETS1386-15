text = "Hello world"

end_with = text.endswith("world")

print(end_with)  # Output: True

# Case-sensitive:
print(text.endswith("World"))  # Output: False

# Using a tuple of suffixes:
suffixes = ("world", "planet")
print(text.endswith(suffixes)) # Output: True

# Checking if ends with either of the values on the iterable
print(text.endswith(("planet", "hello"))) # Output: False

# Using start and end parameters:
print(text.endswith("Hello", 0, 5))  # Output: True (checks "Hello" within the first 5 characters)
print(text.endswith("Hello", 0, 6)) # Output: False (because position [6] is not present on the slice)

# Checking the string with its slice
print(text[0:5].endswith("Hello")) #Output: True

# Empty string
empty_string = ""
print(empty_string.endswith(" ")) # False (Empty so cant end with the string)
