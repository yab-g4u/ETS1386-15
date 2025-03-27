text = "Hello world" #let's use this typical example

start_with = text.startswith("Hello")

print(start_with)  # Output: True

# Case-sensitive:
print(text.startswith("hello"))  # Output: False

# Using a tuple of prefixes:
prefixes = ("Hello", "Goodbye")
print(text.startswith(prefixes)) # Output: True

#Checking if starts with either of the values on the iterable.
print(text.startswith(("GoodBye", "World"))) # False

# Using start and end parameters:
print(text.startswith("world", 6))  # Output: True (starts at index 6)
print(text.startswith("Hello", 1))  #Output: False (starts checking after H)
print(text.startswith("Hello", 0, 5)) #Output: True (only checks 5 first letters)

# Empty String
empty_string = ""
print(empty_string.startswith(" ")) # False (empty so cant start with the string)
