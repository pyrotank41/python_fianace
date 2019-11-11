import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

 # As of pandas 0.24 or higher the recommended way to register the converters is
pd.plotting.register_matplotlib_converters()

style.use('ggplot')

#getting start date and end date in required format
start = dt.datetime(2005,1,1) 
end = dt.datetime(2019,8,13)


df = web.DataReader('TSLA', 'yahoo', start, end) #getting tesla stock from yahoo finanace
df.to_csv('tesla.csv') # write the data to the file

print(df.tail(10))	#printing last 10 data entries from the database
print(df.head(10))	#printing 1st 10 data entries from the data base