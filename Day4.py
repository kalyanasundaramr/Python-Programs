
"""
10 Days Python Challenge
Day 4: FOR LOOP

Topics:
1. Basic for loop
2. range()
3. Loop through a string
4. Loop through a list
5. Loop through a tuple
6. Loop through a dictionary
7. Loop through a set
8. Nested for loop
9. break and continue
10. Practical examples
"""

print("=" * 45)
print("DAY 4: PYTHON FOR LOOP")
print("=" * 45)


# ---------------------------------------------
# 1. BASIC FOR LOOP
# ---------------------------------------------

print("\n1. BASIC FOR LOOP")

for i in range(1, 6):
    print(i)

# range(1, 6) produces 1, 2, 3, 4, 5.
# The ending value 6 is excluded.


# ---------------------------------------------
# 2. USING RANGE()
# ---------------------------------------------

print("\n2. RANGE WITH START, STOP AND STEP")

for i in range(2, 11, 2):
    print(i)

# range(start, stop, step)
# 2 = starting number
# 11 = stopping boundary (excluded)
# 2 = increment by 2


# ---------------------------------------------
# 3. LOOP THROUGH A STRING
# ---------------------------------------------

print("\n3. LOOP THROUGH A STRING")

word = "PYTHON"

for letter in word:
    print(letter)

# Each iteration gives one character.


# ---------------------------------------------
# 4. LOOP THROUGH A LIST
# ---------------------------------------------

print("\n4. LOOP THROUGH A LIST")

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print("I like", fruit)


# ---------------------------------------------
# 5. LOOP THROUGH A TUPLE
# ---------------------------------------------

print("\n5. LOOP THROUGH A TUPLE")

colors = ("Red", "Green", "Blue")

for color in colors:
    print(color)


# ---------------------------------------------
# 6. LOOP THROUGH A DICTIONARY
# ---------------------------------------------

print("\n6. LOOP THROUGH A DICTIONARY")

student = {
    "name": "Arun",
    "age": 20,
    "course": "Python"
}

for key, value in student.items():
    print(key, ":", value)

# items() gives each key and its value.


# ---------------------------------------------
# 7. LOOP THROUGH A SET
# ---------------------------------------------

print("\n7. LOOP THROUGH A SET")

numbers = {10, 20, 30, 40}

for number in numbers:
    print(number)

# A set does not guarantee a particular display order.


# ---------------------------------------------
# 8. NESTED FOR LOOP
# ---------------------------------------------

print("\n8. NESTED FOR LOOP")

for row in range(1, 4):
    for column in range(1, 4):
        print("*", end=" ")
    print()

# The inner loop runs for every outer-loop iteration.


# ---------------------------------------------
# 9. BREAK STATEMENT
# ---------------------------------------------

print("\n9. BREAK STATEMENT")

for number in range(1, 11):
    if number == 5:
        break
    print(number)

# break stops the loop immediately.


# ---------------------------------------------
# 10. CONTINUE STATEMENT
# ---------------------------------------------

print("\n10. CONTINUE STATEMENT")

for number in range(1, 6):
    if number == 3:
        continue
    print(number)

# continue skips the current iteration.


# ---------------------------------------------
# 11. PRACTICAL EXAMPLE: MULTIPLICATION TABLE
# ---------------------------------------------

print("\n11. MULTIPLICATION TABLE")

number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# ---------------------------------------------
# 12. PRACTICAL EXAMPLE: SUM OF NUMBERS
# ---------------------------------------------

print("\n12. SUM OF NUMBERS")

total = 0

for number in range(1, 6):
    total = total + number

print("Sum =", total)

# 1 + 2 + 3 + 4 + 5 = 15


# ---------------------------------------------
# 13. ENUMERATE: INDEX AND VALUE
# ---------------------------------------------

print("\n13. ENUMERATE")

fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


# ---------------------------------------------
# 14. ELSE WITH A FOR LOOP
# ---------------------------------------------

print("\n14. FOR LOOP WITH ELSE")

for number in range(1, 4):
    print(number)
else:
    print("Loop completed normally.")

# The else block runs if the loop finishes normally.
# It does not run if the loop exits using break.


print("\nDay 4 completed successfully!")
