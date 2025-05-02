
# 📘 Dictionary Methods in Python

in this branch i have tried to demonstrate the most commonly used **dictionary methods** in Python 

## 🔧 Methods i Covered with Examples

### 1. `get()`
Safely retrieve a value for a key.

```python
person = {"name": "Alice", "age": 25}
print(person.get("name"))        # Output: Alice
print(person.get("email", "N/A"))  # Output: N/A
````

---

### 2. `keys()`

Get all keys in the dictionary.

```python
person = {"name": "Alice", "age": 25}
print(person.keys())  # Output: dict_keys(['name', 'age'])
```

---

### 3. `values()`

Get all values in the dictionary.

```python
person = {"name": "Alice", "age": 25}
print(person.values())  # Output: dict_values(['Alice', 25])
```

---

### 4. `items()`

Get all key-value pairs.

```python
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 25
```

---

### 5. `pop()`

Remove a key and return its value.

```python
person = {"name": "Alice", "age": 25}
removed_age = person.pop("age")
print(removed_age)  # Output: 25
print(person)       # Output: {'name': 'Alice'}
```

---

### 6. `update()`

Add or update key-value pairs.

```python
person = {"name": "Alice"}
person.update({"age": 26, "email": "alice@example.com"})
print(person)
# Output: {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}
```




