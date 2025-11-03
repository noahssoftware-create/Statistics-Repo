import pandas as pd

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
rounded_z_score = round(float(z_Score,2))
column_value = round(float (rounded_z_score)[-1:])
row_value = round(float(rounded_z_score,1))
