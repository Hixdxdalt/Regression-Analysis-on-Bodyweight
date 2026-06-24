import pandas as pd
import numpy as np
import cvxpy as cp

def merger(pathCal,pathMass):
    df1 = pd.read_csv(pathCal)
    df2 = pd.read_csv(pathMass)

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
    #merged_df.to_csv("Finale.csv", index=False)

    return merged_df


def optimize_calores(weight,fat,kcal):
    carbs = cp.Variable(name="carbs")
    proteins = cp.Variable(name="proteins")
    fats = cp.Variable(name="fats")
    protein_goal = weight * 1.6
    fat_goal = weight * 0.5 if fat == 1 else weight * 1
    
    macros = cp.vstack([carbs, proteins, fats])
    prob = cp.Problem(
        objective = cp.Maximize(carbs)
        constraints = [
            proteins >= protein_goal,
            fats >= fat_goal,
            4*carbs + 4*proteins + 9*fats == kcal,
            carbs >= 0,
            proteins >= 0,
            fats >= 0
        ]
    )
    prob.solve()

    return [carbs.value,proteins.value,fats.value]
