import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

# As of pandas 0.24 or higher the recommended way to register the converters is
pd.plotting.register_matplotlib_converters()

style.use('ggplot')

 #setting index_col = 0 i.e Date, also parsing Date for better graph representation
df = pd.read_csv('tesla.csv', parse_dates=True,index_col=0)

#creating a new data entry

#100ma(moving average): average of last 100 data points 
# windows is the window of data to work on, and min_periods is use to keep minimum boundries soft to provent Nan 
df['100ma'] = df['Close'].rolling(window=100, min_periods=0).mean() #100ma of Closing price 

'''
#dropping all the NaN(not a number).NOT recomended as i am loosing last 100 day's data 
#To not to redefine df(Data frame), we use inplace=true. it's a cleaner approach 
df.dropna(inplace=True) #since we are using min_period in the line above, we dont need this.
'''

#dataplot using matplotlib
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

#plotting plot(x,y)
ax1.plot(df.index, df['Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()

print(df.head())

