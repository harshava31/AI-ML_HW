import numpy as np


def main():
    # 1D Array Creation
    arr_1d = np.array([10, 20, 30, 40, 50])
    print("--- 1D Array Inspection ---")
    print(f"Array:\n{arr_1d}")
    print(f"Shape: {arr_1d.shape}")
    print(f"Size: {arr_1d.size}")
    print(f"Dimensions (ndim): {arr_1d.ndim}")
    print(f"Data Type: {arr_1d.dtype}\n")

    # 2D Array Creation
    arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("--- 2D Array Inspection ---")
    print(f"Array:\n{arr_2d}")
    print(f"Shape: {arr_2d.shape}")
    print(f"Size: {arr_2d.size}")
    print(f"Dimensions (ndim): {arr_2d.ndim}")
    print(f"Data Type: {arr_2d.dtype}")


if __name__ == "__main__":
    main()