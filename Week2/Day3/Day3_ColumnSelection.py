import pandas as pd


def main():
    data = {
        "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
        "Department": ["HR", "IT", "IT", "Sales", "HR"],
        "Salary": [50000, 75000, 80000, 62000, 52000],
        "Experience_Yrs": [2, 5, 7, 3, 1],
    }
    df = pd.DataFrame(data)

    # Selecting a single column (returns Series)
    print("--- Single Column (Name) ---")
    print(df["Name"])

    # Selecting multiple columns (returns DataFrame)
    print("\n--- Multiple Columns (Name, Salary) ---")
    print(df[["Name", "Salary"]])

    # Filtering rows based on condition (Salary > 60000 and IT Department)
    high_salaries = df[df["Salary"] > 60000]
    print("\n--- Filtered Rows (Salary > 60,000) ---")
    print(high_salaries)


if __name__ == "__main__":
    main()