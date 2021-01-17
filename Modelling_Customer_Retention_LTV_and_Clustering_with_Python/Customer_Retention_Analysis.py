# Calculating Customer Retention in Python
'''
# SQL Data Script
select 
date_trunc(d.delivery_date, month) as ref_month,
d.Unique_Stalls as id,
f.signup_month,sum(d.Amount) as revenue from `dmslive.cache_finance_deliveries` d
left join (
    select distinct(Unique_Stalls) as id, min(date_trunc(delivery_date, month)) as signup_month 
    from dmslive.cache_finance_deliveries  group by 1
    ) f on d.Unique_Stalls = f.id
group by 1,2,3
order by 2,1
'''
import pandas as pd
import numpy as np  
from time import strftime
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel('data_for_retention_calculation_monthly.xlsx', parse_dates=['ref_month', 'signup_month'])
print(df.head())
print(df.info())

'''
We need to format the dates and add another column named age. 
Age basically tells us how old was the customer on that day that he was served. 
We add the 1 to it because it makes it more readable, in the sense that age 10 means the customer was on his/her 10th day since signup.
'''
# Calculating the Monthly Age of the customers
df_with_Age = df.copy()
df_with_Age.signup_month = pd.to_datetime(df.signup_month, format='%Y/%m/%d')
df_with_Age.ref_month = pd.to_datetime(df.ref_month, format='%Y/%m/%d')
# age of the customer in Months
df_with_Age['age'] = round((df['ref_month'] - df['signup_month'])/np.timedelta64(1, 'M'))
df_with_Age['age'] = df_with_Age['age'].astype(int) # age column as an integer

# saving the below file once
## df_with_Age.to_excel('data_for_customer_Age_calculated.xlsx') 
print(df_with_Age.head())

# Creating Cohorts
'''
Now we are able to build the cohorts. 
Think of cohorts like buckets where groups of customers are placed according to a certain criteria.

Our cohorts will be created from the signup dates (one for each date). That way they are mutually exclusive. 
We start by using the groupby_ method with signup_date and age, and getting their size. We also need to reset the index.
'''
## using group by - Monthly
monthly_group = df_with_Age.groupby(['signup_month', 'age'])
monthly_cohort_data = monthly_group['id'].size()
monthly_cohort_data = monthly_cohort_data.reset_index()
print(monthly_cohort_data.head())

# Monthly Cohorts Calculations
monthly_cohort_counts = monthly_cohort_data.pivot(index='signup_month', columns='age', values='id')
monthly_cohort_counts.to_excel('monthly_cohort_counts.xlsx') # Run Once
print(monthly_cohort_counts.head())

# We need the base for our retention rate calculation
# Here we just take the first column of weekly_cohort_counts and monthly_cohort_counts
monthly_base = monthly_cohort_counts[0]

# And now we apply the divide method to our cohort_counts, dividing it by the base
monthly_retention = monthly_cohort_counts.divide(monthly_base, axis=0).round(3)
monthly_retention.to_excel('monthly_cohort_retention.xlsx') # Run Once
print(monthly_retention.head())

# Visualiation 1
## User Count heatmap
plt.figure(figsize=(24,12))
plt.title('Monthly Retention Count')
ax = sns.heatmap(data=monthly_cohort_counts, annot=True, vmin=0.0,cmap='Reds')
ax.set_yticklabels(monthly_cohort_counts.index)
fig=ax.get_figure()
fig.savefig("Monthly Retention Counts.png")

# Visualiation 2
## Monthly Retention Rate heatmap
plt.figure(figsize=(24,12))
plt.title('Monthly Retention Table')
ax = sns.heatmap(data=monthly_retention, annot=True, fmt='.0%', vmin=0.0, vmax=1,cmap='Reds')
ax.set_yticklabels(monthly_retention.index)
fig=ax.get_figure()
fig.savefig("Monthly Retention_Rate.png")