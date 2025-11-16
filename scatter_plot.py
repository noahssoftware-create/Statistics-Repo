import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("heart_disease_data.csv")
df = df.sort_values(by=['age', 'chol'], ascending=[True, True])

plt.figure(figsize=(10,6))
plt.title("Scatter Plot of Age vs Cholesterol Levels")
plt.xlabel("Age")
plt.ylabel("Cholesterol Levels")
plt.scatter(df['age'], df['chol'], color='blue', alpha=0.5)
plt.grid(True)
plt.show()