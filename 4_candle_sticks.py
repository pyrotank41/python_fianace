import datetime as dt #for date time
import matplotlib.pyplot as plt #for plotting
from matplotlib import style #for styling graph
from mpl_finance import candlestick_ohlc #for candle stick graph
import matplotlib.dates as mdates #for matplot date (for some reason they use a different fromat for date compared to default date and time format)
import pandas as pd #using pandas
import pandas_datareader.data as web #using this to get data from web (in our case for the time being we are using yahoo finannce)

 # As of pandas 0.24 or higher the recommended way to register the converters is
pd.plotting.register_matplotlib_converters()

style.use('ggplot')

 #setting index_col = 0 i.e Date, also parsing Date for better graph representation
df = pd.read_csv('tesla.csv', parse_dates=True,index_col=0)

#creating a new data entry

#create open high low close dataframe from given 'Adj Close'.
#'10D' here refers to 10 days, resampling cna be done using day hr min secs.

# Because only the adj_close slice of the dataframe is being used, I believe it's calculating the ohlc of only the close values per 10 days.  
# The actual opens, or intra-day high or low points could have been outside those high-low ranges. 
# That's an Important distinction if someone is planning to use this to source data for an actual strategy.
df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True) #resetting index_col to default
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num) #converting Date to mdate using map function

# print(df_ohlc.head())

#dataplot using matplotlib
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date() #converts back to normal date time format

#plotting candlestick_ohlc( on axis, values to plot)
candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')

#plotting filled graph (x point, y point, fill from y=? line)
ax2.fill_between(df_volume.index, df_volume.values, 0)

plt.show()
