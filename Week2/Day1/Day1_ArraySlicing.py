import numpy as np


def main():
    arr = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])

    print("Original 2D Array:\n", arr)

    # Specific element access (row 1, col 2)
    print("\nElement at row 1, col 2:", arr[1, 2])

    # Row extraction
    print("First Row:", arr[0, :])
    print("Last Row:", arr[-1, :])

    # Column extraction
    print("Second Column:", arr[:, 1])

    # Sub-grid Slicing (first 2 rows, first 2 columns)
    print("\n2x2 Sub-grid (Top-Left):\n", arr[:2, :2])


if __name__ == "__main__":
    main()