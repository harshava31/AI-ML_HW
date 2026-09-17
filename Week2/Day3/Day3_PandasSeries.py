import pandas as pd


def main():
    # Creating a Series with custom index labels
    data = [100, 200, 300, 400, 500]
    labels = ["a", "b", "c", "d", "e"]
    s = pd.Series(data, index=labels)

    print("--- Pandas Series ---")
    print(s)

    # Value access and indexing
    print("\nValue at index 'c':", s["c"])
    print("Values from index 'b' to 'd':\n", s["b":"d"])

    # Filtering values greater than 250
    filtered = s[s > 250]
    print("\nFiltered Series (values > 250):\n", filtered)


if __name__ == "__main__":
    main()