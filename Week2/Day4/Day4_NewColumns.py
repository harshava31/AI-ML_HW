import pandas as pd


def main():
    data = {
        "Student": ["Alice", "Bob", "Charlie", "Diana"],
        "Math": [85, 78, 92, 64],
        "Science": [90, 82, 88, 70],
        "English": [88, 75, 95, 80],
    }
    df = pd.DataFrame(data)

    # Creating total marks column
    df["Total_Marks"] = df["Math"] + df["Science"] + df["English"]

    # Creating percentage column (assuming 300 maximum possible marks)
    df["Percentage"] = (df["Total_Marks"] / 300) * 100

    # Creating conditional status column
    df["Status"] = df["Percentage"].apply(
        lambda x: "Pass" if x >= 75 else "Needs Improvement"
    )

    print("--- DataFrame with New Calculated Columns ---")
    print(df)


if __name__ == "__main__":
    main()