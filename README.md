# 📘 Python Tuples Assignment

This assignment explores the basics and common operations of **tuples in Python**. Tuples are immutable sequences used to store collections of items. The examples below demonstrate various methods and features of tuples using easy-to-understand code.

---

## 🔧 Tuple Methods and Operations

### 1. `count()`

The `count()` method returns the number of times a specific value appears in a tuple.

```
vehicles = ("car", "bike", "car", "bus", "car")
print(vehicles.count("car"))  # Output: 3

```
---

### 2. `index()`

The `index()` method returns the index of the first occurrence of a value in the tuple.
```
grades = ("A", "B", "C", "B", "A")
print(grades.index("C"))  # Output: 2

```
---

### 3. `Tuple Unpacking`

Tuple unpacking assigns the elements of a tuple to multiple variables in a single line.
```
coordinates = (12.4, 45.8)
x, y = coordinates
print(f"x = {x}, y = {y}")  # Output: x = 12.4, y = 45.8
```

---

### 4. `Tuple Concatenation`

You can combine two or more tuples using the + operator.
```
odd_numbers = (1, 3, 5)
even_numbers = (2, 4, 6)
combined = odd_numbers + even_numbers
print(combined)  # Output: (1, 3, 5, 2, 4, 6)

```
---

### 5. `len()` with Tuples

The len() function returns the total number of items in the tuple.
```
days = ("Mon", "Tue", "Wed", "Thu", "Fri")
print(len(days))  # Output: 5
```

---
