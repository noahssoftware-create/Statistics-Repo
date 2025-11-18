import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Scatter plot of data
df = pd.read_csv("data.csv")

m = float(input ("imput slope m: "))
b = float(input ("input intercept b: "))

#Calculate the Sum of Squared Errors
def SSE(x, true_y, m, b):
    # y1 is the slope of the predicted line y2 is the actual data points
    slopes_y = m * x + b
    return np.sum((slopes_y - true_y) ** 2)