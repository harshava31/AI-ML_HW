import numpy as np


def main():
    a = np.array([10, 20, 30, 40])
    b = np.array([2, 4, 5, 8])

    print(f"Array A: {a}")
    print(f"Array B: {b}\n")

    # Element-wise operations
    print("Addition (A + B):      ", a + b)
    print("Subtraction (A - B):   ", a - b)
    print("Multiplication (A * B):", a * b)
    print("Division (A / B):      ", a / b)

    # Universal math functions
    print("\nSquare root of A:", np.sqrt(a))
    print("Sum of all elements in A:", np.sum(a))


if __name__ == "__main__":
    main()