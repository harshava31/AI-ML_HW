def generate_table(number: int):
    print(f"--- Multiplication Table for {number} ---")
    for i in range(1, 11):
        print(f"{number} x {i:2d} = {number * i}")


def main():
    try:
        num = int(input("Enter a number: "))
        generate_table(num)
    except ValueError:
        print("Invalid input! Please enter an integer.")


if __name__ == "__main__":
    main()