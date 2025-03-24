# Python String Methods Assignment

in this assignment i have demonstrated the use of various Python string methods. Each method is explained with a brief description and a code example.

## 1. `str.isdecimal()`

**Purpose:** Checks if all characters in the string are decimal digits (0-9).

**Return Value:** `True` if all characters are decimal digits and the string is not empty; `False` otherwise.

**Example:**


number_string = "12345"
is_decimal = number_string.isdecimal()
print(is_decimal) # Output: True

empty_string = ""
is_decimal = empty_string.isdecimal()
print(is_decimal) # Output: False

 ```

▌2. str.isalnum()

Purpose: Checks if all characters in the string are alphanumeric (letters or numbers) and the string is not empty.

Return Value: True if all characters are alphanumeric and the string is not empty; False otherwise.

Example:


```

pro = "python3"
result = pro.isalnum()
print(result) # Output: True

pro2 = "python 3" #has a space between the words
result = pro2.isalnum()
print(result) #output: False

```

▌3. str.isnumeric()

Purpose: Checks if all characters in the string are numeric characters (including digits, fractions, and other numeric symbols) and the string is not empty.

Return Value: True if all characters are numeric and the string is not empty; False otherwise.

Example:


```

number_string = "12345"
is_numeric = number_string.isnumeric()
print(is_numeric) # Output: True

fraction_string = "½"
is_numeric = fraction_string.isnumeric()
print(is_numeric) # Output: True

decimal_string = "3.14"
is_numeric = decimal_string.isnumeric()
print(is_numeric) # Output: False (contains a decimal point)

```

▌4. str.capitalize()

Purpose: Returns a copy of the string with the first character capitalized and the rest lowercased.

Return Value: A new string with the first character capitalized.

Example:


```
sentence = "the quick brown fox"
capitalized_sentence = sentence.capitalize()
print(capitalized_sentence) # Output: The quick brown fox

```

▌5. str.count(substring)

Purpose: Returns the number of non-overlapping occurrences of a substring within the string.

Return Value: An integer representing the number of occurrences.

Example:


```
text = "hello world hello"
count_of_hello = text.count("hello")
print(count_of_hello) # Output: 2

count_of_o = text.count("o")
print(count_of_o) # Output: 3
```

▌6. str.startswith(prefix)

Purpose: Checks if the string starts with the specified prefix.

Return Value: True if the string starts with the prefix; False otherwise.

Example:


```
text = "Hello world"
starts_with_hello = text.startswith("Hello")
print(starts_with_hello) # Output: True

starts_with_goodbye = text.startswith("Goodbye")
print(starts_with_goodbye) # Output: False

```

▌7. str.endswith(suffix)

Purpose: Checks if the string ends with the specified suffix.

Return Value: True if the string ends with the suffix; False otherwise.

Example:


```
text = "Hello world"
ends_with_world = text.endswith("world")
print(ends_with_world) # Output: True

ends_with_hello = text.endswith("hello")
print(ends_with_hello) # Output: False

```

▌8. str.swapcase()

Purpose: Returns a copy of the string with uppercase characters converted to lowercase and vice versa.

Return Value: A new string with the case of each character swapped.

Example:


```
text = "Hello World"
swapped_case = text.swapcase()
print(swapped_case) # Output: hELLO wORLD

```

▌9. str.title()

Purpose: Returns a copy of the string where the first letter of each word is capitalized (title case).

Return Value: A new string in title case.

Example:


```

my_string = "this is a test string"
title_case_string = my_string.title()
print(title_case_string) # Output: This Is A Test String

```

```
