def print_right_triangle(rows: int):
    print("--- Right Triangle Pattern ---")
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()


def print_inverted_triangle(rows: int):
    print("\n--- Inverted Triangle Pattern ---")
    for i in range(rows, 0, -1):
        for j in range(i):
            print("*", end="")
        print()


def print_pyramid(rows: int):
    print("\n--- Pyramid Pattern ---")
    for i in range(1, rows + 1):
        # Print leading spaces for alignment
        for j in range(rows - i):
            print(" ", end="")
        # Print stars
        for k in range(2 * i - 1):
            print("*", end="")
        print()


def main():
    n = 5
    print_right_triangle(n)
    print_inverted_triangle(n)
    print_pyramid(n)


if __name__ == "__main__":
    main()