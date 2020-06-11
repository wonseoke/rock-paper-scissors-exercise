# game.py
""" 
options = ["rock", "paper", "scissors"]

choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

if choice in options:
    print("YOU CHOSE", choice)
else:
    raise ValueError("OOPS - Please type 'rock', or 'paper', or 'scissors' (without using using quotation marks).")
 """

# adapted from: https://matplotlib.org/gallery/pie_and_polar_charts/pie_features.html
# adapted from: https://plot.ly/python/getting-started/#initialization-for-offline-plotting

import matplotlib.pyplot as plt
import seaborn as sns

# The .set() function changes the plot's aesthetics
# For more information and specific styles see: https://seaborn.pydata.org/generated/seaborn.set.html
sns.set(style="darkgrid")

# The .load_dataset() function uses a built-in dataset
tips = sns.load_dataset("tips") # this is a pandas DataFrame!
print(type(tips)) #> <class 'pandas.core.frame.DataFrame'>
print(tips.columns.tolist()) #> ['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']

# The .relplot() function creates a relational plot using an x-axis and y-axis
# It also allows you to specify the markers, colors, sizes, etc.
sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips)

# Need to explicitly "show" the chart window
plt.show()