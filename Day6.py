
"""
10 Days Python Challenge
DAY 6: PYTHON DICTIONARY

Topics:
1. Create a dictionary
2. Access values
3. Add and update items
4. Remove items
5. Dictionary methods
6. Loop through a dictionary
7. Check whether a key exists
8. Dictionary length and built-in functions
9. Combine dictionaries
10. Convert two lists into a dictionary
11. Nested dictionaries
12. Dictionary comprehension
13. Practical student marks program
"""

print("=" * 50)
print("DAY 6: PYTHON DICTIONARY")
print("=" * 50)


# --------------------------------------------------
# 1. CREATE A DICTIONARY
# --------------------------------------------------

print("\n1. CREATE A DICTIONARY")

student = {
    "name": "Arun",
    "age": 20,
    "course": "Python",
    "mark": 85
}

print("Student:", student)
print("Data type:", type(student))
print("Number of items:", len(student))


# --------------------------------------------------
# 2. ACCESS VALUES
# --------------------------------------------------

print("\n2. ACCESS VALUES")

print("Name:", student["name"])
print("Age:", student["age"])

# get() safely returns None if the key is missing.
print("City:", student.get("city"))

# get() can also return a default value.
print("City with default:", student.get("city", "Not provided"))

# student["city"] raises KeyError if the key is missing.
# print(student["city"])


# --------------------------------------------------
# 3. ADD AND UPDATE ITEMS
# --------------------------------------------------

print("\n3. ADD AND UPDATE ITEMS")

student["city"] = "Chennai"
print("After adding city:", student)

student["age"] = 21
print("After updating age:", student)

# update() adds or updates multiple key-value pairs.
student.update({"mark": 90, "course": "Python Programming"})
print("After update():", student)


# --------------------------------------------------
# 4. REMOVE ITEMS
# --------------------------------------------------

print("\n4. REMOVE ITEMS")

details = {
    "name": "Priya",
    "age": 22,
    "city": "Chennai",
    "course": "Python"
}

print("Original:", details)

# pop(): remove a key and return its value.
removed_value = details.pop("age")
print("Removed age:", removed_value)
print("After pop():", details)

# popitem(): remove and return the last inserted pair.
removed_pair = details.popitem()
print("Removed pair:", removed_pair)
print("After popitem():", details)

# del: delete a specific key.
del details["city"]
print("After del:", details)

# clear(): remove all items.
details.clear()
print("After clear():", details)


# --------------------------------------------------
# 5. IMPORTANT DICTIONARY METHODS
# --------------------------------------------------

print("\n5. DICTIONARY METHODS")

employee = {
    "name": "Ravi",
    "department": "IT",
    "salary": 40000
}

print("Original:", employee)

# keys(): all keys
print("Keys:", employee.keys())

# values(): all values
print("Values:", employee.values())

# items(): key-value pairs
print("Items:", employee.items())

# get(): retrieve a value safely
print("Name:", employee.get("name"))

# setdefault(): add a key only if it is missing
employee.setdefault("city", "Chennai")
print("After setdefault():", employee)

# Existing value is not overwritten by setdefault().
employee.setdefault("name", "Kumar")
print("Name remains:", employee["name"])

# copy(): shallow copy
employee_copy = employee.copy()
employee_copy["name"] = "Kumar"

print("Original employee:", employee)
print("Copied employee:", employee_copy)


# --------------------------------------------------
# 6. LOOP THROUGH A DICTIONARY
# --------------------------------------------------

print("\n6. LOOP THROUGH A DICTIONARY")

student = {
    "name": "Arun",
    "age": 20,
    "course": "Python",
    "mark": 90
}

# Loop through keys.
print("\nKeys:")

for key in student:
    print(key)

# Loop through values.
print("\nValues:")

for value in student.values():
    print(value)

# Loop through keys and values.
print("\nKey-value pairs:")

for key, value in student.items():
    print(key, ":", value)


# --------------------------------------------------
# 7. CHECK WHETHER A KEY EXISTS
# --------------------------------------------------

print("\n7. CHECK KEY EXISTENCE")

if "name" in student:
    print("The name key exists.")

if "city" not in student:
    print("The city key does not exist.")


# --------------------------------------------------
# 8. LENGTH AND BUILT-IN FUNCTIONS
# --------------------------------------------------

print("\n8. BUILT-IN FUNCTIONS")

marks = {
    "Arun": 85,
    "Priya": 95,
    "Kumar": 75
}

print("Marks:", marks)
print("Number of students:", len(marks))

# max() and min() on a dictionary use its keys.
print("Alphabetically greatest student name:", max(marks))
print("Alphabetically smallest student name:", min(marks))

# For highest and lowest marks, use values().
print("Highest mark:", max(marks.values()))
print("Lowest mark:", min(marks.values()))
print("Total marks:", sum(marks.values()))
print("Average marks:", sum(marks.values()) / len(marks))


# --------------------------------------------------
# 9. COMBINE DICTIONARIES
# --------------------------------------------------

print("\n9. COMBINE DICTIONARIES")

dict1 = {"name": "Arun", "age": 20}
dict2 = {"city": "Chennai", "course": "Python"}

# update() modifies dict1.
dict1.update(dict2)
print("Combined using update():", dict1)

# The | operator creates a new combined dictionary.
dict3 = {"a": 1, "b": 2}
dict4 = {"c": 3, "d": 4}

combined = dict3 | dict4
print("Combined using |:", combined)


# --------------------------------------------------
# 10. CONVERT TWO LISTS INTO A DICTIONARY
# --------------------------------------------------

print("\n10. TWO LISTS TO DICTIONARY")

keys = ["name", "age", "city"]
values = ["Priya", 22, "Chennai"]

result = {}

for i in range(len(keys)):
    result[keys[i]] = values[i]

print("Dictionary using a for loop:", result)

# A shorter alternative uses zip().
result2 = {}

for key, value in zip(keys, values):
    result2[key] = value

print("Dictionary using zip():", result2)


# --------------------------------------------------
# 11. NESTED DICTIONARY
# --------------------------------------------------

print("\n11. NESTED DICTIONARY")

students = {
    "student1": {
        "name": "Arun",
        "mark": 85
    },
    "student2": {
        "name": "Priya",
        "mark": 95
    }
}

print("All students:", students)

print("First student:", students["student1"])
print("First student name:", students["student1"]["name"])
print("Second student mark:", students["student2"]["mark"])

print("\nAll student details:")

for student_id, details in students.items():
    print(student_id)

    for key, value in details.items():
        print(" ", key, ":", value)


# --------------------------------------------------
# 12. DICTIONARY COMPREHENSION
# --------------------------------------------------

print("\n12. DICTIONARY COMPREHENSION")

numbers = [1, 2, 3, 4, 5]

# Create a dictionary of number and square.
squares = {number: number ** 2 for number in numbers}
print("Squares:", squares)

# Keep only even numbers and their squares.
even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print("Even squares:", even_squares)


# --------------------------------------------------
# 13. PRACTICAL STUDENT MARKS PROGRAM
# --------------------------------------------------

print("\n13. STUDENT MARKS PROGRAM")

student_marks = {
    "Arun": 85,
    "Priya": 95,
    "Kumar": 58,
    "Meena": 72
}

for name, mark in student_marks.items():
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "E"

    print(name, "| Mark:", mark, "| Grade:", grade)


print("\nDay 6 completed successfully!")
