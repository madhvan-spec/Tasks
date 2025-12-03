def get_number(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Please enter a valid number.")

def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")

    num1 = get_number("Enter first number: ")
    op = input("Enter operation (+, -, *, /): ")

    # Checking if operator is valid or not
    while op not in ["+", "-", "*", "/"]:
        print("Invalid operation. Please choose one of +, -, *, /")
        op = input("Enter operation: ")

    num2 = get_number("Enter second number: ")

    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Error: Division by zero."
        result = num1 / num2

    return f"Result: {result}"


print(calculator())
