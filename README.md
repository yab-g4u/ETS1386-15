# Python String Methods Assignment

In this assignment, I have demonstrated the use of various Python string methods. Each method is explained with a brief description and a code example.

## 1. str.isdecimal()

**Purpose:** Checks if all characters in the string are decimal digits (0-9).

**Return Value:** True if all characters are decimal digits and the string is not empty; False otherwise.

**Example:**

```python
number_string = "12345"
is_decimal = number_string.isdecimal()
print(is_decimal) # Output: True

empty_string = ""
is_decimal = empty_string.isdecimal()
print(is_decimal) # Output: False
```

## 2. str.isalnum()

**Purpose:** Checks if all characters in the string are alphanumeric (letters or numbers) and the string is not empty.

**Return Value:** True if all characters are alphanumeric and the string is not empty; False otherwise.

**Example:**

```python
pro = "python3"
result = pro.isalnum()
print(result) # Output: True

pro2 = "python 3" # has a space between the words
result = pro2.isalnum()
print(result) # Output: False
```

## 3. str.isnumeric()

**Purpose:** Checks if all characters in the string are numeric characters (including digits, fractions, and other numeric symbols) and the string is not empty.

**Return Value:** True if all characters are numeric and the string is not empty; False otherwise.

**Example:**

```python
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

## 4. str.capitalize()

**Purpose:** Returns a copy of the string with the first character capitalized and the rest lowercased.

**Return Value:** A new string with the first character capitalized.

**Example:**

```python
sentence = "the quick brown fox"
capitalized_sentence = sentence.capitalize()
print(capitalized_sentence) # Output: The quick brown fox
```

## 5. str.count(substring)

**Purpose:** Returns the number of non-overlapping occurrences of a substring within the string.

**Return Value:** An integer representing the number of occurrences.

**Example:**

```python
text = "hello world hello"
count_of_hello = text.count("hello")
print(count_of_hello) # Output: 2

count_of_o = text.count("o")
print(count_of_o) # Output: 3
```

## 6. str.startswith(prefix)

**Purpose:** Checks if the string starts with the specified prefix.

**Return Value:** True if the string starts with the prefix; False otherwise.

**Example:**

```python
text = "Hello world"
starts_with_hello = text.startswith("Hello")
print(starts_with_hello) # Output: True

starts_with_goodbye = text.startswith("Goodbye")
print(starts_with_goodbye) # Output: False
```

## 7. str.endswith(suffix)

**Purpose:** Checks if the string ends with the specified suffix.

**Return Value:** True if the string ends with the suffix; False otherwise.

**Example:**

```python
text = "Hello world"
ends_with_world = text.endswith("world")
print(ends_with_world) # Output: True

ends_with_hello = text.endswith("hello")
print(ends_with_hello) # Output: False
```

## 8. str.swapcase()

**Purpose:** Returns a copy of the string with uppercase characters converted to lowercase and vice versa.

**Return Value:** A new string with the case of each character swapped.

**Example:**

```python
text = "Hello World"
swapped_case = text.swapcase()
print(swapped_case) # Output: hELLO wORLD
```

## 9. str.title()

**Purpose:** Returns a copy of the string where the first letter of each word is capitalized (title case).

**Return Value:** A new string in title case.

**Example:**

```python
my_string = "this is a test string"
title_case_string = my_string.title()
print(title_case_string) # Output: This Is A Test String
```

## 10. str.replace(old, new)

**Purpose:** Replaces all occurrences of a specified substring with another substring.

**Return Value:** A new string with replacements made.

**Example:**

```python
text = "I love Python"
new_text = text.replace("Python", "Java")
print(new_text) # Output: I love Java
```

## 11. str.strip()

**Purpose:** Removes leading and trailing whitespace from the string.

**Return Value:** A new string with whitespace removed.

**Example:**

```python
text = "  hello world  "
stripped_text = text.strip()
print(stripped_text) # Output: "hello world"
```

## 12. str.lstrip()

**Purpose:** Removes leading whitespace from the string.

**Return Value:** A new string with leading whitespace removed.

**Example:**

```python
text = "  hello world"
lstripped_text = text.lstrip()
print(lstripped_text) # Output: "hello world"
```

## 13. str.rstrip()

**Purpose:** Removes trailing whitespace from the string.

**Return Value:** A new string with trailing whitespace removed.

**Example:**

```python
text = "hello world  "
rstripped_text = text.rstrip()
print(rstripped_text) # Output: "hello world"
```

## 14. str.split(separator)

**Purpose:** Splits the string into a list of substrings based on a specified separator.

**Return Value:** A list of substrings.

**Example:**

```python
text = "apple,banana,grape"
fruits = text.split(",")
print(fruits) # Output: ['apple', 'banana', 'grape']
```

## 15. str.join(iterable)

**Purpose:** Joins elements of an iterable into a single string, using the given string as a separator.

**Return Value:** A new string with the iterable elements joined.

**Example:**

```python
words = ["Hello", "World"]
joined_text = " ".join(words)
print(joined_text) # Output: Hello World
```

