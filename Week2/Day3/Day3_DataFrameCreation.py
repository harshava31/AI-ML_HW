import pandas as pd


def main():
    # Creating a DataFrame from a dictionary of lists
    student_data = {
        "Name": ["Alice", "Bob", "Charlie", "Diana"],
        "Age": [20, 22, 21, 23],
        "Score": [88.5, 92.0, 79.5, 95.0],
    }
    df = pd.DataFrame(student_data)

    print("--- DataFrame ---")
    print(df)

    # Inspecting rows and columns
    print("\nShape (rows, cols):", df.shape)
    print("Columns:", list(df.columns))
    print("Index:", df.index)


if __name__ == "__main__":
    main()