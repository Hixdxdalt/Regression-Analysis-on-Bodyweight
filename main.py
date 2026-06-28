import pandas as pd
import numpy as np
import os
import helper

while True:
    print("Welcome to Calorie Calculator.\n1.) Merge calories with weight into CSV\n2.) Find macronutrients based on caloric goal.\n3.) Fit observed weight trends\n4.) Find TDEE through ODE and integration\n5.) Project future weight changes\n6.) Exit")
    user_input = int(input("select an option: "))

    if user_input == 1:
        cal_lst = input("insert path to calories CSV file: ")
        weight_lst = input("insert path to weight CSV file: ")

        if os.path.isfile(cal_lst) and os.path.isfile(weight_lst):
            final_df = helper.merger(cal_lst,weight_lst)
            final_df.to_csv("Final.csv", index=False)
        else:
            print("Invalid file directories.")

    elif user_input == 2:
        weight = float(input("Insert your bodyweight in KG: "))
        while True:
            print("Please select one of the following:\n1.) Low fat\n2.) High fat")
            fat = int(input("Select an option: "))
            if fat == 1 or fat == 2:
                break
            else:
                print("Invalid input, please try again.")
        kcal = float(input("Insert your caloric goal: "))
        C,P,F = helper.optimize_calories(weight,fat,kcal)
        print(f"Here is the optimized macronutrient profile:\nCarbohydrates = {C:1f}\nProteins = {P:1f}\nFats = {F:1f}")

    else:
        break
    