
"""
Day 4 Python Assignment
Topic: Dictionary + For Loop

Assignment 1:
Use a dictionary in a for loop.

Assignment 2:
Convert two lists into a dictionary using a for loop.
"""


# ==================================================
# ASSIGNMENT 1: USE A DICTIONARY IN A FOR LOOP
# ==================================================

print("=" * 50)
print("ASSIGNMENT 1: DICTIONARY WITH FOR LOOP")
print("=" * 50)

# Create a dictionary
student = {
    "name": "Arun",
    "age": 20,
    "course": "Python",
    "city": "Chennai"
}

# Print the dictionary
print("\nStudent Dictionary:")
print(student)

# Loop through dictionary keys
print("\n1. Display Keys:")

for key in student:
    print(key)

# Loop through dictionary values
print("\n2. Display Values:")

for value in student.values():
    print(value)

# Loop through both keys and values
print("\n3. Display Keys and Values:")

for key, value in student.items():
    print(key, ":", value)


# ==================================================
# ASSIGNMENT 2: CONVERT TWO LISTS INTO A DICTIONARY
# ==================================================

print("\n" + "=" * 50)
print("ASSIGNMENT 2: TWO LISTS TO DICTIONARY")
print("=" * 50)

# Create two lists
keys = ["name", "age", "course", "city"]

values = ["Arun", 20, "Python", "Chennai"]

# Create an empty dictionary
student_details = {}

# Use a for loop to combine the lists
for i in range(len(keys)):
    student_details[keys[i]] = values[i]

# Display the result
print("\nKeys List:")
print(keys)

print("\nValues List:")
print(values)

print("\nConverted Dictionary:")
print(student_details)

# Display each dictionary item
print("\nStudent Details:")

for key, value in student_details.items():
    print(key, ":", value)


# ==================================================
# BONUS: CONVERT TWO LISTS USING ZIP()
# ==================================================

print("\n" + "=" * 50)
print("BONUS: USING ZIP() WITH A FOR LOOP")
print("=" * 50)

products = ["Laptop", "Mouse", "Keyboard"]
prices = [50000, 500, 1200]

product_prices = {}

for product, price in zip(products, prices):
    product_prices[product] = price

print("\nProduct Prices:")

for product, price in product_prices.items():
    print(product, ":", price)


print("\nAssignment completed successfully!")
