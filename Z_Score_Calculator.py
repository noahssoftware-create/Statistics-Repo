import pandas as pd
from decimal import *
import numpy as np
#import csv for z table
ztable_df = pd.read_csv("ztable_stats.csv")

#Create variables inside Z score calculator
data_point = float(input("Individual value: "))
mu = float(input("Population mean: "))
std = float(input("Standard deviation: "))

# Add Z score calculation
def z_Score(data_point, mu, std):
    z = (data_point - mu) / std
    return z

z_Score = z_Score(data_point,mu,std)


# Find the column& row for z  table data frame
row_column = np.trunc(z_Score * 100)
row_column = (row_column / 100)
print(f"Z score: {row_column}")