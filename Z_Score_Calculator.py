import pandas as pd
from decimal import *
import numpy as np

# Import csv for z table
ztable_df = pd.read_csv("ztable_stats.csv",sep=";",index_col="Z")

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
z_Score = float(round(z_Score,2))

# Find the column& row for z  table data frame
ztable_row = (z_Score * 10)
ztable_row = float((np.trunc(ztable_row))/10)

ztable_column = (ztable_row - z_Score)
ztable_column = float(round(ztable_column,2))

# Convert the column veriable into a positive
if ztable_column < 0:
    ztable_column = ztable_column * -1
else:
    pass

find_column_str = f".{int(ztable_column * 100) :02d}"

probability = ztable_df.at[ztable_row,find_column_str]


# Print Z Score and Probability of getting that value
print(f"Z score: {z_Score}")
print(probability)
print(find_column_str)