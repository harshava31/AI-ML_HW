import pandas as pd


def main():
    data = {
        "emp_id": [101, 102, 103, 104, 105],
        "emp_name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
        "sal": [70000, 50000, 85000, 62000, 50000],
        "age": [28, 34, 25, 30, 22],
    }
    df = pd.DataFrame(data)

    print("--- Original DataFrame ---")
    print(df)

    # Renaming columns
    df_renamed = df.rename(
        columns={
            "emp_id": "Employee_ID",
            "emp_name": "Name",
            "sal": "Salary",
            "age": "Age",
        }
    )
    print("\n--- Renamed DataFrame ---")
    print(df_renamed)

    # Sorting by a single column (Salary descending)
    sorted_by_salary = df_renamed.sort_values(by="Salary", ascending=False)
    print("\n--- Sorted by Salary (Descending) ---")
    print(sorted_by_salary)

    # Sorting by multiple columns (Salary ascending, then Age ascending)
    sorted_multi = df_renamed.sort_values(
        by=["Salary", "Age"], ascending=[True, True]
    )
    print("\n--- Sorted by Salary (Ascending) and Age (Ascending) ---")
    print(sorted_multi)


if __name__ == "__main__":
    main()