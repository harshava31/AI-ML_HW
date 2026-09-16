import numpy as np


def main():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print(f"Matrix A:\n{A}\n")
    print(f"Matrix B:\n{B}\n")

    print(f"Addition (A + B):\n{A + B}\n")
    print(f"Matrix Multiplication (A @ B):\n{A @ B}")


if __name__ == "__main__":
    main()