import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#download and sort data
df = pd.read_csv("spy_historical_data.csv")
df = df.sort_values("Date")

#Grab sample size group and mean of the sample
sample_size = len(df)
sample_mean = df["Close"].mean()

#Equation for the impirical rule
sample_STD = np.sqrt(np.sum((df["Close"] - sample_mean)**2) / (sample_size-1))

print(sample_STD)