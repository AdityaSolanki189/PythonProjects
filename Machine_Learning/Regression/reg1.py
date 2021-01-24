import pandas as pd
import quandl
# editing features
df = quandl.get("BATS/BATS_GOOGL", authtoken="o-C8ufyhAhE_CEQmDhpx")
df['Percentage'] = (df['Total Volume'] - df['Short Volume']) / df['Total Volume'] * 100

print(df.head(10))
