import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('googleplaystore.csv')
df.info()

cat = df.Category.unique()
print(cat)

