def calculator():
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        operator = input("Enter the operator ('+', '-', '*', '/', '%'): ")

        if operator == '+':
            result = number1 + number2
            print(f"Sum: {result}")
        elif operator == '-':
            result = number1 - number2
            print(f"Subtraction: {result}")
        elif operator in ['*', 'x', 'X']:
            result = number1 * number2
            print(f"Multiplication: {result}")
        elif operator == '/':
            if number2 != 0:
                result = number1 / number2
                print(f"Division: {result}")
            else:
                print("Error: Division by zero")
        elif operator == '%':
            result = number1 % number2
            print(f"Remainder: {result}")
        else:
            print("Invalid operator")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    calculator()