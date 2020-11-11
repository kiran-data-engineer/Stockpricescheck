import yfinance as yf
from pandas import DataFrame
import matplotlib.pyplot as plt


data = yf.download("RDSB.L", start="2020-10-01", end="2020-10-11")


df = DataFrame(data, columns=['Date', 'High'])
df.plot(x='Date', y='High', kind='scatter')
plt.show()
print(df)
