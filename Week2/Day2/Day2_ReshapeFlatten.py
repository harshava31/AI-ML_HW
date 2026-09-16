import numpy as np


def main():
    original = np.arange(1, 13)
    print(f"Original 1D Array:\n{original}\n")

    reshaped = original.reshape(3, 4)
    print(f"Reshaped 3x4 Array:\n{reshaped}\n")

    flattened = reshaped.flatten()
    print(f"Flattened Array: {flattened}")

    raveled = reshaped.ravel()
    print(f"Raveled Array:   {raveled}")


if __name__ == "__main__":
    main()