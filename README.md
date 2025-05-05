# 📘 Python Sets 
Sets are unordered collections of unique elements that support powerful operations like unions, intersections, and more.

---

## 🔧 Set Methods and Operations

### 1. `add()`

Adds an element to a set if it's not already present.

```
colors = {"red", "green"}
colors.add("blue")
print(colors)  # Output: {'red', 'green', 'blue'}
```

### 2. `remove()`
Removes a specified item. Raises an error if the item is not found.

```
cities = {"New York", "London", "Tokyo"}
cities.remove("London")
print(cities)  # Output: {'New York', 'Tokyo'}
```
### 3. `discard()`
Removes an item if it exists. Does not raise an error if it doesn't.

```
sports = {"football", "basketball", "cricket"}
sports.discard("hockey")
print(sports)  # Output: {'football', 'basketball', 'cricket'}
```
### 4.  `union()`
Returns a new set with all elements from both sets (no duplicates).

```
set1 = {"apple", "banana"}
set2 = {"banana", "cherry"}
result = set1.union(set2)
print(result)  # Output: {'apple', 'banana', 'cherry'}
```
### 5. `intersection()`
Returns only the items that exist in both sets.

```
weekdays = {"Mon", "Tue", "Wed", "Thu", "Fri"}
office_days = {"Wed", "Thu", "Fri"}
print(weekdays.intersection(office_days))  # Output: {'Wed', 'Thu', 'Fri'}
```
### 6. `difference()`
Returns items only in the first set and not in the second.

```
students = {"Alice", "Bob", "Charlie"}
present_today = {"Alice", "Charlie"}
absent_students = students.difference(present_today)
print(absent_students)  # Output: {'Bob'}
```
