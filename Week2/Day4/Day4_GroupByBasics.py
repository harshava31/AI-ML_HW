import pandas as pd


def main():
    data = {
        "Employee": [
            "Alice",
            "Bob",
            "Charlie",
            "Diana",
            "Ethan",
            "Fiona",
            "George",
        ],
        "Department": ["IT", "HR", "IT", "Sales", "HR", "Sales", "IT"],
        "Salary": [75000, 50000, 85000, 62000, 52000, 68000, 90000],
        "Experience_Yrs": [3, 5, 7, 2, 4, 6, 8],
    }
    df = pd.DataFrame(data)

    print("--- Original Data ---")
    print(df)

    # Count of employees per department
    print("\n--- Employee Count by Department ---")
    print(df.groupby("Department")["Employee"].count())

    # Average salary by department
    print("\n--- Average Salary by Department ---")
    print(df.groupby("Department")["Salary"].mean())

    # Aggregating multiple metrics
    print("\n--- Detailed Summary Stats by Department ---")
    dept_summary = df.groupby("Department").agg(
        Total_Employees=("Employee", "count"),
        Avg_Salary=("Salary", "mean"),
        Avg_Experience=("Experience_Yrs", "mean"),
    )
    print(dept_summary)


if __name__ == "__main__":
    main()