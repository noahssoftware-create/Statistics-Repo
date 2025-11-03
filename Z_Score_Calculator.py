import pandas as pd
from decimal import *
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
column_value = float(round(z_Score[-1]))
row_value = float(round(z_Score,1))

print(column_value)