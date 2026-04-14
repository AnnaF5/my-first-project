# Simple Calculator
print("=== Simple Calculator ===")

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
1
# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Cannot divide by zero"

# Display results
print(f"\n--- Results ---")
print(f"Sum: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
