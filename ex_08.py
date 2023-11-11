def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        operation = int(input("Enter the operation number: "))
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == 1:
            result = num1 + num2
        elif operation == 2:
            result = num1 - num2
        elif operation == 3:
            result = num1 * num2
        elif operation == 4:
            if num2 == 0:
                raise ZeroDivisionError("Error: Division by zero is not allowed.")
            result = num1 / num2
        else:
            print("Invalid operation selection.")
            return

        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except ZeroDivisionError as e:
        print(e)

calculator()
