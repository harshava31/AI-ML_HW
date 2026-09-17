import os
import pandas as pd


def main():
    csv_file = "sample_data.csv"

    # Create a simple CSV file if it doesn't exist
    if not os.path.exists(csv_file):
        data = {
            "ID": [1, 2, 3, 4, 5, 6, 7],
            "Department": ["HR", "IT", "IT", "Sales", "HR", "Sales", "IT"],
            "Salary": [50000, 75000, 80000, 62000, 52000, 68000, 85000],
        }
        pd.DataFrame(data).to_csv(csv_file, index=False)

    # Reading the CSV file
    df = pd.read_csv(csv_file)

    print("--- Head (First 5 Rows) ---")
    print(df.head())

    print("\n--- Tail (Last 2 Rows) ---")
    print(df.tail(2))

    print("\n--- Data Info ---")
    df.info()

    print("\n--- Summary Statistics ---")
    print(df.describe())


if __name__ == "__main__":
    main()