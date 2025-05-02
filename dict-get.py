person = {"name": "yab", "age": 25}
print(person.get("name"))       # yab
print(person.get("email", "N/A"))  # N/A (default value if key not found)
