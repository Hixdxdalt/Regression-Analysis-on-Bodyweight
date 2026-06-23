import pandas as pd
import numpy as np

df1 = pd.read_csv("Raw data/Calories.csv")
df2 = pd.read_csv("Raw data/Weight.csv")

# Convert dates
df1["Date"] = pd.to_datetime(df1["Date"])
df2["Date"] = pd.to_datetime(df2["Date"])

# Daily calories
daily_calories = (
    df1.groupby("Date", as_index=False)["Calories"]
       .sum()
)

daily_calories["Calories"] = np.ceil(
    daily_calories["Calories"]
).astype(int)

# Daily weight
daily_weight = (
    df2.groupby("Date", as_index=False)["Weight"]
       .mean()
)

# Merge using calories as the date list
merged_df = pd.merge(
    daily_calories,
    daily_weight,
    on="Date",
    how="left"
)

# Forward fill weights
merged_df["Weight"] = merged_df["Weight"].ffill()

# Save
merged_df.to_csv("Merged_Calories_Weight.csv", index=False)