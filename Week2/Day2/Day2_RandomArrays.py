import numpy as np


def main():
    np.random.seed(42)

    rand_floats = np.random.rand(2, 3)
    print("--- Random Floats (0 to 1) ---")
    print(rand_floats, "\n")

    rand_ints = np.random.randint(10, 50, size=(3, 3))
    print("--- Random Integers (10 to 49) ---")
    print(rand_ints, "\n")

    rand_normal = np.random.randn(4)
    print("--- Normal Distribution Samples ---")
    print(rand_normal)


if __name__ == "__main__":
    main()