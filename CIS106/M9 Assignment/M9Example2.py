# Example 2 - Calculator

def calculate(num1, num2, op_code):
    if op_code.upper() == 'A':
        return num1 + num2
    elif op_code.upper() == 'S':
        return num1 - num2
    elif op_code.upper() == 'M':
        return num1 * num2
    elif op_code.upper() == 'D':
        if num2 == 0:
            return -999
        return num1 / num2
    else:
        return None

while True:
    entry = input("Enter first number (or STOP to quit): ")

    if entry.upper() == "STOP":
        break

    num1 = float(entry)
    num2 = float(input("Enter second number: "))
    code = input("Enter operation code (A,S,M,D): ")

    result = calculate(num1, num2, code)

    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Operation: {code}")
    print(f"Result: {result}")

    if result == -999:
        print("Error: Cannot divide by zero.")