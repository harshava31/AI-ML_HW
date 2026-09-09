def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def get_number(prompt):
    
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid numerical value.")


def main():
    while True:
        print("\n" + "=" * 30)
        print("      MENU CALCULATOR      ")
        print("=" * 30)
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        print("=" * 30)

        choice = input("Enter your choice (1-5): ").strip()

        # Handle Exit
        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break

        # Check for valid menu choice using match-case
        match choice:
            case "1" | "2" | "3" | "4":
                # Get valid numbers from user
                num1 = get_number("Enter first number: ")
                num2 = get_number("Enter second number: ")

                # Perform operation based on choice
                match choice:
                    case "1":
                        result = add(num1, num2)
                        print(f"\nResult: {num1} + {num2} = {result}")

                    case "2":
                        result = subtract(num1, num2)
                        print(f"\nResult: {num1} - {num2} = {result}")

                    case "3":
                        result = multiply(num1, num2)
                        print(f"\nResult: {num1} * {num2} = {result}")

                    case "4":
                        try:
                            result = divide(num1, num2)
                            print(f"\nResult: {num1} / {num2} = {result}")
                        except ZeroDivisionError as e:
                            print(f"\nError: {e}")

            case _:
                print("\nInvalid choice! Please select an option between 1 and 5.")


if __name__ == "__main__":
    main()