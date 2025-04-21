# Problem Statement: Develop a simple command-line calculator that performs basic arithmetic operations (addition, subtraction, multiplication, division).
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

print("Welcome to the Simple Command-Line Calculator!")

while True:
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
        continue

    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result:.2f}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result:.2f}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result:.2f}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}" 
              if isinstance(result, str) 
              else f"{num1} / {num2} = {result:.2f}")
    elif choice == '5':
        print("Thank you for using the calculator. Goodbye!")
        break
    else:
        print("Invalid input. Please select a valid option.")
