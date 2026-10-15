"""
Python Learning Program:
Mutable and Immutable Data Types

Mutable   = Can be changed after creation.
Immutable = Cannot be changed after creation.
"""


# ==================================================
# 1. INTEGER (int) - IMMUTABLE
# ==================================================

print("\n1. INTEGER (int) - IMMUTABLE")

a = 10
print("Original value:", a)
print("Data type:", type(a))

a = a + 5
print("After adding 5:", a)

# Python creates/assigns the resulting integer value.
# Integers cannot be modified in place.


# ==================================================
# 2. FLOAT (float) - IMMUTABLE
# ==================================================

print("\n2. FLOAT (float) - IMMUTABLE")

price = 99.50
print("Original value:", price)
print("Data type:", type(price))

price = price + 10.50
print("After adding:", price)


# ==================================================
# 3. STRING (str) - IMMUTABLE
# ==================================================

print("\n3. STRING (str) - IMMUTABLE")

name = "Python"
print("Original value:", name)
print("Data type:", type(name))

# Strings cannot be changed character by character.
# name[0] = "J"  # Uncomment to see TypeError

name = name + " Programming"
print("After concatenation:", name)


# ==================================================
# 4. BOOLEAN (bool) - IMMUTABLE
# ==================================================

print("\n4. BOOLEAN (bool) - IMMUTABLE")

is_learning = True
print("Original value:", is_learning)
print("Data type:", type(is_learning))

is_learning = False
print("After reassignment:", is_learning)


# ==================================================
# 5. LIST (list) - MUTABLE
# ==================================================

print("\n5. LIST (list) - MUTABLE")

numbers = [10, 20, 30]
print("Original list:", numbers)
print("Data type:", type(numbers))

numbers[0] = 100
print("After updating first item:", numbers)

numbers.append(40)
print("After adding an item:", numbers)

numbers.remove(20)
print("After removing an item:", numbers)


# ==================================================
# 6. TUPLE (tuple) - IMMUTABLE
# ==================================================

print("\n6. TUPLE (tuple) - IMMUTABLE")

coordinates = (10, 20, 30)
print("Original tuple:", coordinates)
print("Data type:", type(coordinates))

# Tuples do not support item assignment.
# coordinates[0] = 100  # Uncomment to see TypeError

# You can create a new tuple instead.
coordinates = (100, 20, 30)
print("New tuple:", coordinates)


# ==================================================
# 7. DICTIONARY (dict) - MUTABLE
# ==================================================

print("\n7. DICTIONARY (dict) - MUTABLE")

student = {"name": "Arun", "age": 20}
print("Original dictionary:", student)
print("Data type:", type(student))

student["age"] = 21
print("After updating age:", student)

student["course"] = "Python"
print("After adding a key:", student)

del student["age"]
print("After deleting age:", student)


# ==================================================
# 8. SET (set) - MUTABLE
# ==================================================

print("\n8. SET (set) - MUTABLE")

colors = {"red", "green", "blue"}
print("Original set:", colors)
print("Data type:", type(colors))

colors.add("yellow")
print("After adding an item:", colors)

colors.discard("red")
print("After removing an item:", colors)

# Sets contain unique values.
colors.add("green")
print("After adding green again:", colors)


# ==================================================
# 9. BYTES (bytes) - IMMUTABLE
# ==================================================

print("\n9. BYTES (bytes) - IMMUTABLE")

data = bytes([65, 66, 67])
print("Original bytes:", data)
print("Data type:", type(data))
print("Decoded text:", data.decode("utf-8"))

# data[0] = 90  # Uncomment to see TypeError


# ==================================================
# 10. BYTEARRAY (bytearray) - MUTABLE
# ==================================================

print("\n10. BYTEARRAY (bytearray) - MUTABLE")

data = bytearray([65, 66, 67])
print("Original bytearray:", data)
print("Data type:", type(data))

data[0] = 90
print("After changing first byte:", data)
print("Decoded text:", data.decode("utf-8"))


# ==================================================
# 11. FROZENSET (frozenset) - IMMUTABLE
# ==================================================

print("\n11. FROZENSET (frozenset) - IMMUTABLE")

fixed_numbers = frozenset([1, 2, 3])
print("Original frozenset:", fixed_numbers)
print("Data type:", type(fixed_numbers))

# fixed_numbers.add(4)  # Uncomment to see AttributeError


# ==================================================
# 12. RANGE (range) - IMMUTABLE
# ==================================================

print("\n12. RANGE (range) - IMMUTABLE")

values = range(1, 5)
print("Range values:", list(values))
print("Data type:", type(values))

# A range's start, stop, and step cannot be modified.
# Create a new range to use different values.


# ==================================================
# FINAL SUMMARY
# ==================================================

print("\n" + "=" * 50)
print("SUMMARY OF MUTABLE AND IMMUTABLE TYPES")
print("=" * 50)

print("""
MUTABLE:
1. list
2. dict
3. set
4. bytearray

IMMUTABLE:
1. int
2. float
3. complex
4. bool
5. str
6. tuple
7. bytes
8. frozenset
9. range
10. NoneType

Important:
- Mutable objects can be changed in place.
- Immutable objects cannot be changed in place.
- Reassigning a variable is different from modifying
  the object it previously referred to.
""")
