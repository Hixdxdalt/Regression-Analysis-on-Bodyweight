import pandas as pd
import numpy as np
import os
import helper

while True:
    print("Welcome to Calorie Calculator.\n1.) Merge calories with weight into CSV\n2.) Find macronutrients based on caloric goal.\n3.) Fit observed weight trends\n4.) Find ODE and integration\n5.) Project future weight changes\n6.) Exit")
    user_input = int(input("select an option: "))

    if user_input == 1:
        cal_lst = input("insert path to calories CSV file: ")
        weight_lst = input("insert path to weight CSV file: ")

        if os.path.isfile(cal_lst) and os.path.isfile(weight_lst):
            final_df = helper.merger(cal_lst,weight_lst)
            final_df.to_csv("Final.csv", index=False)
        else:
            print("Invalid file directories.")

    else:
        break

    