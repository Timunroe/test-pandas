import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})

# close
plt.close('all')

file_name = "data.csv"

df = pd.read_csv(file_name,
                 keep_default_na=False,
                 na_values='0')

df['Month'] = pd.to_datetime(df['Month'])
df['Avg'] = df['Articles'].expanding().mean()
df.set_index('Month', inplace=True)
# print(df.dtypes)
# print(df.columns.values)
# print(df.head(3))

plt.figure()
df.plot()
# plt.tight_layout()
plt.grid(b=True, which='major', axis='y')
plt.xlabel('Months')
plt.ylabel('Articles')
plt.savefig('test.png')

# close
plt.close('all')
