
"""
10 Days Python Challenge
Topic: Conditional Statements

Learn:
1. Simple if statement
2. if-else statement
3. if-elif-else statement
4. Nested if statement
5. Ternary conditional expression
"""

print("=" * 45)
print("PYTHON CONDITIONAL STATEMENTS")
print("=" * 45)


# --------------------------------------------------
# 1. SIMPLE IF STATEMENT
# --------------------------------------------------

print("\n1. SIMPLE IF STATEMENT")

age = 20

if age >= 18:
    print("You are eligible to vote.")

# Explanation:
# The message prints only when age >= 18 is True.


# --------------------------------------------------
# 2. IF-ELSE STATEMENT
# --------------------------------------------------

print("\n2. IF-ELSE STATEMENT")

number = 7

if number % 2 == 0:
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")

# Explanation:
# % gives the remainder.
# If the remainder is 0, the number is even.
# Otherwise, the number is odd.


# --------------------------------------------------
# 3. IF-ELIF-ELSE STATEMENT
# --------------------------------------------------

print("\n3. IF-ELIF-ELSE STATEMENT")

mark = 85

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

print("Mark:", mark)
print("Grade:", grade)

# Explanation:
# Python checks conditions from top to bottom.
# The first True condition determines the grade.


# --------------------------------------------------
# 4. NESTED IF STATEMENT
# --------------------------------------------------

print("\n4. NESTED IF STATEMENT")

age = 22
has_id = True

if age >= 18:
    print("You meet the minimum age requirement.")

    if has_id:
        print("You have an ID. Entry is permitted.")
    else:
        print("Please bring your ID.")
else:
    print("You are below the required age.")

# Explanation:
# An if statement inside another if statement
# is called a nested if statement.


# --------------------------------------------------
# 5. TERNARY CONDITIONAL EXPRESSION
# --------------------------------------------------

print("\n5. TERNARY CONDITIONAL EXPRESSION")

age = 16

result = "Adult" if age >= 18 else "Minor"

print("Age:", age)
print("Category:", result)

# Equivalent longer version:
#
# if age >= 18:
#     result = "Adult"
# else:
#     result = "Minor"


# --------------------------------------------------
# 6. COMBINE CONDITIONS USING AND / OR
# --------------------------------------------------

print("\n6. COMBINING CONDITIONS")

age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive, subject to local rules.")
else:
    print("You do not meet the age or license requirement.")

# AND: Both conditions must be True.
# OR: At least one condition must be True.

temperature = 35

if temperature < 20 or temperature > 30:
    print("The temperature is outside the 20-30 range.")


# --------------------------------------------------
# 7. USER INPUT EXAMPLE
# --------------------------------------------------

print("\n7. USER INPUT EXAMPLE")

user_mark = int(input("Enter your mark (0-100): "))

if user_mark < 0 or user_mark > 100:
    print("Invalid mark. Enter a value from 0 to 100.")
elif user_mark >= 90:
    print("Grade A")
elif user_mark >= 80:
    print("Grade B")
elif user_mark >= 70:
    print("Grade C")
elif user_mark >= 60:
    print("Grade D")
else:
    print("Grade E")

print("\nConditional statements lesson completed!")
