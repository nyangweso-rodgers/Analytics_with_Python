# Panel Data
## What is a Panel Data?
'''
--Panel data is also a time based dataset.
The difference is that, in addition to time series, it also contains one or more related variables that are measured for the same time periods.
Typically, the columns present in panel data contain explanatory variables that can be helpful in predicting the Y, provided those columns will be available at the future forecasting period.
'''
from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

# an example of a panel data is as shown below:
# # dataset source: https://github.com/rouseguy
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/MarketArrivals.csv')
df = df.loc[df.market=='MUMBAI', :]
df.head()
# df.to_excel('sample.xlsx') # save the result into an excel file