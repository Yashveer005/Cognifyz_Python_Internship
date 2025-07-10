def add(a,b):      #BASIC CALCULATOR
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a/b

def modulus(a, b):
    if b == 0:
        raise ValueError("Cannot perform modulus with zero.")
    return a % b

def calculator():
    print("Basic Calculator")
    print("Enter 'q' at any time to quit.")

    while True:
        try:
            num1 = float(input("Enter the first number:"))
            operator = input("Enter the operator (+, -, *, /, %):")
            if operator == 'q':
                 break
            num2 = float(input("Enter the second number:"))

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            elif operator == '%':
                result = modulus(num1, num2)
            else:
                print("Invalid operator. Please try again.")
                continue

            print(f"Result:{num1} {operator} {num2} = {result}\n")

        except ValueError as e:
            print("Invalid input. Please enter valid numbers.")
        except ZeroDivisionError as e:
            print("Error: cannot divide by zero.")
        except Exception as e:
            print(f"An error occured: {e}")

if __name__ == "__main__":
    calculator()