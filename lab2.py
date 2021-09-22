"""
Grace Michael
DS2500: Programming with Data
Lab 2
"""

import seaborn as sns

sns.get_dataset_names()

data = sns.load_dataset('diamonds')

print(data)

# Variables
carat = data.carat
price = data.price

# Correlation
correlation = carat.corr(price)

print('Correlation:', correlation)

# Linear regression model

import scipy.stats as stats
import matplotlib.pyplot as plt

diamond = stats.linregress(x=carat, y=price)
print('Carats vs Price', diamond)
slope = diamond.slope
intercept = diamond.intercept
predictions = [slope * x + intercept for x in carat]

# Seaborn regression plot
plt.figure(figsize=(12,8))
sns.regplot(x=data.carat, y=data.price, color='#0ABAB5', scatter_kws={'s':5})
plt.title("Diamond Prices Based on Carats")
plt.xlabel("Diamond Size in Carats")
plt.ylabel("Price ($)")
plt.show()

# Plot
rounded_carats = carat.round()
sns.boxplot(x=rounded_carats, y='price', palette=['#ffd1dc', '#0ABAB5', '#77dd77', '#b19cd9', '#ffb347', '#FDFD96'], data=data)
plt.title("Diamond Prices Based on Carats (Rounded) Boxplots")
plt.xlabel("Diamond Size in Carats (rounded to whole integers)")
plt.ylabel("Price ($)")
sns.despine(offset=10, trim=True)
plt.show()

'''
I wanted to show a box and whisker plot in order to show the distribution of the data, such as the
minimum, maximum, median, and interquartile ranges, for the carats. I rounded the carats as most of the
diamonds are not the same exact size, in order to show the distributions for each integer size. This shows
how large the pricing ranges within similar sizes, their large ranges and outliers showing that their are other variables
to determining diamond price other than the number of carats.
'''
