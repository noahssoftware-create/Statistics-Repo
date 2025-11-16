import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Scatter plot of data
df = pd.read_csv("data.csv")

m = input ("imput slope m: ")
b = input ("input intercept b: ")

#Calculate the Sum of Squared Errors
def SSE(x, y1, m, b):
    """ y1 is the slope of the predicted line
    y2 is the actual data points """
    y1 = m * x + b
    SSE = sum((y1 - y2) ** 2)
    return SSE