import pandas as pd
from decimal import *
import numpy as np

# Import csv for z table
ztable_df = pd.read_csv("ztable_stats.csv")

# Create variables inside Z score calculator
data_point = float(input("Individual value: "))
mu = float(input("Population mean: "))
std = float(input("Standard deviation: "))

# Add Z score calculation
def z_Score(data_point, mu, std):
    z = (data_point - mu) / std
    return z

# Round Z score to the 2nd decimal
z_Score = z_Score(data_point,mu,std)
z_Score = round(z_Score,2)

# Find the column& row for z  table data frame
ztable_row = (z_Score * 10)
ztable_row = (np.trunc(ztable_row))/10

ztable_column = (ztable_row - z_Score)
ztable_column = round(ztable_column,2)


# Print Z Score and Probability of getting that value
print(f"Z score: {z_Score}")
