import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('googleplaystore.csv')
df.info()

cat = df.Category.unique()
print(cat)

plt.figure(figsize=(12, 12))
most_cat = df.Category.value_counts()
sns.barplot(x=most_cat, y=most_cat.index, data=df)
