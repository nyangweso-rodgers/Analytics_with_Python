# RFM Analysis
## Import appropriate modules
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
plt.style.use('seaborn-white')
import seaborn as sns 
import datetime as dt

df = pd.read_excel('data_for_RFM_score_analysis.xlsx', parse_dates=['date'])
print(df.head())
#print(df.describe())

## Generating Summary Statistics: 
## Method 1:
def describe(df):
    return pd.concat([df.describe().T,
                      df.mad().rename('mad'),# mean absolute deviation
                      df.skew().rename('skew'), # skewness
                      df.kurt().rename('kurt'), # kurtosis
                     ], axis=1).T
RFM_Summary_Stats = describe(df)
print(RFM_Summary_Stats)
# RFM_Summary_Stats.to_excel('RFM_Summary_Statistics+Table.xlsx') # Save the Summary Stats to an excel table

## Method 2
stats = df.describe()
## appending interquartile range instead of recalculating it
stats.loc['IQR'] = stats.loc['75%'] - stats.loc['25%'] 
stats = stats.append(df.reindex(stats.columns, axis=1).agg(['skew', 'mad', 'kurt']))
print(stats)


# Creating the RFM Table

## Getting first and last order date
print("Min Date: ", df['date'].min(), "Max Date: ", df['date'].max()) # Min Date:  2020-04-01 00:00:00 Max Date:  2020-09-25 00:00:00
'''
In the dataset, the last delivery date is September 25, 2020, we have used this date as NOW date to calculate recency.
'''
NOW = dt.datetime(2020, 9, 25)

rfm_table = df.groupby('id').agg(
                                    {'date': lambda x: (NOW - x.max()).days, # Recency
                                     'id': lambda x: len(x), # Frequency
                                     'sales': lambda x: x.sum() # Monetary
                                     }
                                    )
rfm_table['date'] = rfm_table['date'].astype(int)
rfm_table.rename(columns = {'date': 'recency',
                            'id': 'frequency',
                            'sales': 'monetary_value'}, inplace = True)
                            
# Now, we have RFM values with respect to each customer
# rfm_table.to_excel('Report_RFM_Table.xlsx')
print(rfm_table.head())

# Summary Statistics for our RFM Table
def describe(rfm_table):
    return pd.concat([rfm_table.describe().T,
                      # mean absolute deviation
                      rfm_table.mad().rename('mad'),
                      rfm_table.skew().rename('skew'),
                      rfm_table.kurt().rename('kurt'),
                     ], axis=1).T
print(describe(rfm_table))

quantiles = rfm_table.quantile(q = [0.25, 0.5, 0.75])
# Converting quantiles to a dictionary, easier to use.
quantiles = quantiles.to_dict()
print(quantiles)

## RFM Segmentation
RFM_Segment = rfm_table.copy()
# Arguments (x = value, p = recency, monetary_value, frequency, k = quartiles dict)
def R_Class(x,p,d):
    if x <= d[p][0.25]:
        return 4
    elif x <= d[p][0.50]:
        return 3
    elif x <= d[p][0.75]: 
        return 2
    else:
        return 1

# Arguments (x = value, p = recency, monetary_value, frequency, k = quartiles dict)
def FM_Class(x,p,d):
    if x <= d[p][0.25]:
        return 1
    elif x <= d[p][0.50]:
        return 2
    elif x <= d[p][0.75]: 
        return 3
    else:
        return 4

RFM_Segment['R_Quartile'] = RFM_Segment['recency'].apply(R_Class, args=('recency',quantiles,))
RFM_Segment['F_Quartile'] = RFM_Segment['frequency'].apply(FM_Class, args=('frequency',quantiles,))
RFM_Segment['M_Quartile'] = RFM_Segment['monetary_value'].apply(FM_Class, args=('monetary_value',quantiles,))

RFM_Segment['RFMClass'] = RFM_Segment.R_Quartile.map(str)  + RFM_Segment.F_Quartile.map(str)  + RFM_Segment.M_Quartile.map(str)
RFM_Segment = RFM_Segment.sort_values(by = ['RFMClass', 'monetary_value'], ascending = [True, False])

# Uncomment the below code to save the output to an excel file
#RFM_Segment.to_excel('Report_RFM_Segments.xlsx')
print(RFM_Segment.head())

'''
Another possibility is to combine the scores to create one score (eg. 4+1+1). 
This will create a score between 3 and 12. Here the advantage is that each of the scores got same importance. 
However some scores will have many segements as constituents (eg - 413 ad 431)
'''
RFM_Segment['TotalScore'] = RFM_Segment['R_Quartile'] + RFM_Segment['F_Quartile'] + RFM_Segment['M_Quartile']
#RFM_Segment.to_excel('Report_RFM_Segments.xlsx')
print(RFM_Segment.head())
## Example
print(RFM_Segment.groupby('TotalScore').agg('monetary_value').mean())



# Questions 7 Answers of Interests
'''
RFM segmentation readily answers these questions for your business…:

* Who are my best customers?
* Which customers are at the verge of churning?
* Who are lost customers that you don’t need to pay much attention to?
* Who are your loyal customers?
* Which customers you must retain?
* Who has the potential to be converted into more profitable customers?
* Which group of customers is most likely to respond to your current campaign?
'''

## 1. Q. Who are my best customers?
print(RFM_Segment[RFM_Segment['RFMClass']=='444'].sort_values('monetary_value',  ascending=False).head())

## 2. Q. Which customers are at the verge of churning? i.e., Customers whose recency are low:
print(RFM_Segment[RFM_Segment['R_Quartile'] <= 2 ].sort_values('monetary_value', ascending=False).head(5))

## 3. Q. Who are the lost customers? ie.., Customers whose recency, frequency, as well as monetary values are low.
print(RFM_Segment[RFM_Segment['RFMClass']=='111'].sort_values('recency', ascending=False).head(5))

## 4. Q. Who are loyal customers? ie., Customers with _high frequency_ value
print(RFM_Segment[RFM_Segment['F_Quartile'] >= 3 ].sort_values('monetary_value', ascending=False).head(5))

## Visualizations
ax1 = plt.subplot(2, 3, 1) # number of row = 1, number of columns = 2, subplot order = 1 
ax1 = RFM_Segment.groupby('TotalScore').agg('monetary_value').mean().plot(kind = 'bar', colormap = 'Blues_r')
ax1.set_ylabel('Monetary Value')
ax1.set_xlabel('Total Score')

ax2 = plt.subplot(2, 3, 2)
ax2 = RFM_Segment.groupby('TotalScore').agg('frequency').mean().plot(kind='bar', colormap='Blues_r')
ax2.set_ylabel('Frequency')
ax2.set_xlabel('Total Score')

ax3 = plt.subplot(2, 3, 3)
ax3 = RFM_Segment.groupby('TotalScore').agg('recency').mean().plot(kind='bar', colormap='Blues_r')
ax3.set_ylabel('Recency')
ax3.set_xlabel('Total Score')