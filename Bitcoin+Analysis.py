
# coding: utf-8

# # Cryptocurrency Price Analysis
# 
# 
# For the first part of the project, I extracted the Bitcoin prices from Yahoo Finance: https://finance.yahoo.com/quote/BTC-USD/ and key words frequency from Google Trends: https://trends.google.com/trends/explore?q=bitcoin&geo=US. Yahoo Finance indicates the closing prices,and opening prices which are crucial to understanding the volatility of the asset. Whereas,the Google trends indicate the key word freqency or "interest over time". Furthermore, any user can download the data into a CSV file. 
# 
# To parse the data from yahoo, I simply used "pdr.get_data_yahoo('asset', start = 'startdate', end = 'enddate') which extracts the closing price of the month and organzied by monthly. 
# The financial data are organzied by year and the closing price of the month. For example, I have gotten the data on this page: https://finance.yahoo.com/quote/BTC-USD/history?p=BTC-USD. This allows us to collect the data automatically just by importing datetime. We weren't able to automatically load the data from Google trends automatically so we have to download the data into a CSV file to read the data. 
# 
# Because this is Cryptocurrency, we are working a lot with the closing price to analyze the data. We parse the yahoo financial page containing the closing prices then the parse the data from the CSV (the google trend file) into a Pandaframe to organzie the data. 
# 
# 
# Objective from first part of the project:
# - Extract BTC prices from Yahoo Finance and key words frequency from Google Trends
# - Manipulate, transform, and merge datasets to prepare variables
# - Run simple regression against the key words 'Bitcoin'
# - Analyze regression statistics and conclude the significance
# 
# 

# In[215]:

import numpy as np
import pandas as pd
import pandas_datareader.data as pdr
from datetime import datetime

from scipy import stats
import statsmodels.api as sm 

import matplotlib.pyplot as plt


# In[154]:

#Setting the end date to today
end = datetime.today()

#Start date set to one year back
start = datetime(end.year-5,end.month,end.day)

#using yahoo finance to grab cryptocurrency data
BTC = pdr.get_data_yahoo('BTC-USD',start = "2014-1-1",end = datetime.today(),interval='m')
# ETH = pdr.DataReader('ETH-USD','yahoo',start,end)
# LTC = pdr.DataReader('LTC-USD','yahoo',start,end)


# In[155]:

#Look at top 5 rows of Bitcoin data
BTC.tail(5)


# Parse the data by using pdr.get_data_yahoo(.......) then extract them into 6
# different catergories such as High, Low, Open, Close..etc

# In[44]:

#Set the figure sizes
plt.rcParams['figure.figsize'] = (10,8)


# In[216]:

#Plot the Bitcoin price movements over the past 5 years
BTC['Adj Close'].plot(legend = True);


# In[47]:

#Plot 10,20,and 50 days moving average with daily Bitcoin prices

ma_days = [10,20,50]

for ma in ma_days:
     column_name = "MA %s days"%(str(ma))        
     BTC[column_name] = BTC['Adj Close'].rolling(window=ma,center=False).mean()

BTC[['Adj Close','MA 10 days','MA 20 days','MA 50 days']].plot(legend=True);



# ### Don't Run This Section - Use Pytrend package to extract daily google searches data (Didn't work for montly frequencies)

# In[55]:

from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)

kw_list = ["Bitcoin"]


# In[60]:

search_df = pytrends.get_historical_interest(kw_list, year_start=2019, month_start=1, day_start=1, year_end=2019, month_end=3, day_end=1,cat=0, geo='', gprop='', sleep=0.5)
#search_df = pytrends.interest_over_time()
search_df.head(5)


# ### Download Bitcoin Google Seraches from Google Trends 

# In[170]:

BTC_searches= pd.read_csv('multiTimeline.csv',skiprows=1)


# In[178]:

BTC_searches.columns = ['Date','Bitcoin']


# ### Combine Two Pandas Dataframes

# In[191]:

BTC_prices = BTC['Adj Close'].iloc[:-1]
BTC_prices


# In[195]:

df = pd.concat([BTC_prices.reset_index(drop=True),BTC_searches.reset_index(drop=True)], axis=1)


# In[203]:

#df = df.set_index('Date')
df.head(3)


# In[221]:

#Draw the scatter plot with Bitcoin searches as an independent variable, 
#and Bitcoin average monthly prices as a dependent variable
X = df['Bitcoin']
Y = df['Adj Close']
plt.scatter(X,Y)
plt.axis([0,120,0,15000])

#Draw the trend line
z = np.polyfit(X,Y,1)
p = np.poly1d(z)
plt.plot(X,p(X),"r")
plt.show()


# ### Simple Linear Regression Statistics of Price of Bitcoin and Google Trend Freqency Search
# The figure above clearly indicates that there is a strong linear relationship between the Closing Price of the Bitcoin and the Freqency search of "Bitcoin" on  Google. Furthermore, this graph indicates that freqency search on Google can be a good price predictor. More would be explained below.

# In[218]:

#Apply statsmodel to run regression and conclude detailed stats
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()


# In[219]:

reg.summary()


# In[220]:

#Or use scipy to run linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)
stats.linregress(X,Y)


# ### Insights:
# 1. This univariate regression explains that 64.8% of the Bitcoin prices is explained by 'Bitcoin' frequencies in Google searches
# 2. p-values for the slope and intercept are both smaller than 0.01. The model has decent prediction power for future Bitcoin prices.
