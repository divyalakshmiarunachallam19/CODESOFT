# Simple Calculator Program

# Function to perform arithmetic operations
def calculate(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operation"

# Main program
print("Welcome to the simple calculator!")

# Input: two numbers and an operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an operation: add, subtract, multiply, divide")
operation = input("Enter operation: ").strip().lower()

# Perform calculation
result = calculate(num1, num2, operation)

# Display the result
print(f"The result of {operation}ing {num1} and {num2} is: {result}")
