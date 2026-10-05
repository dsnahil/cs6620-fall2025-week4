"""Simple calculator application."""


def add(first_number, second_number):
    """Add two numbers"""
    return first_number + second_number


def subtract(first_number, second_number):
    """Subtract two numbers"""
    return first_number - second_number


def multiply(first_number, second_number):
    """Multiply two numbers"""
    return first_number * second_number


def divide(first_number, second_number):
    """Divide two numbers"""
    if second_number == 0:
        raise ValueError("Cannot divide by zero")
    return first_number / second_number


def calculate(operation, first_number, second_number):
    """Perform calculation based on operation"""
    if operation == "add":
        result = add(first_number, second_number)
    elif operation == "subtract":
        result = subtract(first_number, second_number)
    elif operation == "multiply":
        result = multiply(first_number, second_number)
    elif operation == "divide":
        result = divide(first_number, second_number)
    else:
        raise ValueError(f"Unknown operation: {operation}")

    return result


if __name__ == "__main__":
    print("Simple Calculator")
    print("-" * 20)

    result1 = calculate("add", 10, 5)
    print(f"10 + 5 = {result1}")

    result2 = calculate("multiply", 7, 3)
    print(f"7 * 3 = {result2}")

    print("Calculator completed successfully!")