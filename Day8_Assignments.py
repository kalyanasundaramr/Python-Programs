
# Day 8 Assignment: Arithmetic Calculator
# Using Python Functions

# 1. Addition
def add(a, b):
    return a + b


# 2. Subtraction
def subtract(a, b):
    return a - b


# 3. Multiplication
def multiply(a, b):
    return a * b


# 4. Division
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


# 5. Modulus (remainder)
def modulus(a, b):
    if b == 0:
        return "Error: Cannot calculate modulus with zero"
    return a % b


# 6. Exponentiation (power)
def power(a, b):
    return a ** b


# 7. Floor division
def floor_divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a // b


# Main calculator program
def calculator():
    print("================================")
    print("       PYTHON CALCULATOR")
    print("================================")

    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Power (**)")
        print("7. Floor Division (//)")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "8":
            print("Thank you for using the calculator!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid choice. Please select 1 to 8.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        elif choice == "5":
            result = modulus(num1, num2)
        elif choice == "6":
            result = power(num1, num2)
        elif choice == "7":
            result = floor_divide(num1, num2)

        print("Result:", result)


# Start the program
if __name__ == "__main__":
    calculator()
