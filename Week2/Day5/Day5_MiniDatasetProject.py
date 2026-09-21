import numpy as np
import pandas as pd


def main():
    # 1. Create a raw sales dataset with missing values and inconsistencies
    raw_data = {
        "Transaction_ID": [101, 102, 103, 104, 105, 106, 107, 108],
        "Region": ["North", "South", "East", "West", "North", np.nan, "East", "South"],
        "Units_Sold": [12, 15, np.nan, 20, 10, 8, 25, 18],
        "Unit_Price": [100.0, 150.0, 120.0, np.nan, 100.0, 200.0, 120.0, 150.0],
    }
    df = pd.DataFrame(raw_data)
    print("--- Raw Dataset ---")
    print(df)

    # 2. Data Cleaning
    df["Region"] = df["Region"].fillna("Unknown")
    df["Units_Sold"] = df["Units_Sold"].fillna(df["Units_Sold"].median())
    df["Unit_Price"] = df["Unit_Price"].fillna(df["Unit_Price"].mean())

    # 3. Data Analysis & Feature Engineering
    df["Total_Sales"] = df["Units_Sold"] * df["Unit_Price"]

    print("\n--- Cleaned Dataset with Calculated Total Sales ---")
    print(df)

    # 4. Summary Aggregation by Region
    region_summary = df.groupby("Region").agg(
        Total_Revenue=("Total_Sales", "sum"),
        Avg_Units_Sold=("Units_Sold", "mean"),
        Transaction_Count=("Transaction_ID", "count"),
    )

    print("\n--- Regional Sales Summary ---")
    print(region_summary)


if __name__ == "__main__":
    main()