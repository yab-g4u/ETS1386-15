# isdecimal() - the string method i chose to start with

the purpose of isdecimal is it checks if all characters in the string are decimal digits.

for example:
number_string = "12345"
is_decimal = number_string.isdecimal() #we expect it to return true since the elements in the string are decimals.therefore it Returns True

#if we try empty strings

empty_strings = ""
is_decimal = empty_strings.isdecimal() # Returns False
