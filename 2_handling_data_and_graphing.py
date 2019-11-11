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
print(df.head())

# df.plot() #plot all the parameters in the dataset. 
df['Close'].plot() #plotting only one parameter form the database.  
plt.show() #show the plot