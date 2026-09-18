import numpy as np
import pandas as pd


def main():
    # Creating a DataFrame with missing (NaN) values
    data = {
        "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
        "Age": [25, np.nan, 30, 22, np.nan],
        "Score": [85, 90, np.nan, 88, 95],
        "Department": ["HR", "IT", "Sales", np.nan, "IT"],
    }
    df = pd.DataFrame(data)

    print("--- Original DataFrame with Missing Values ---")
    print(df)

    # Identifying missing values
    print("\n--- Missing Value Count per Column ---")
    print(df.isnull().sum())

    # Filling missing values
    df_filled = df.copy()
    df_filled["Age"] = df_filled["Age"].fillna(df_filled["Age"].mean())
    df_filled["Score"] = df_filled["Score"].fillna(0)
    df_filled["Department"] = df_filled["Department"].fillna("Unassigned")

    print("\n--- DataFrame After Filling Missing Values ---")
    print(df_filled)

    # Dropping rows with missing values
    df_dropped = df.dropna()
    print("\n--- DataFrame After Dropping Rows with Missing Values ---")
    print(df_dropped)


if __name__ == "__main__":
    main()