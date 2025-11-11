import pandas as pd

df = pd.read_csv('https://gist.githubusercontent.com/DRALVINANG/5821855d6bcce977fc7f7638bb7ea9a3/raw/9d5bf33a581bf81a8319baf9d677eef309a2d7e9/TSLA%2520Stock%2520Price%2520(2020).csv')
df
#-------------------------------------------------------------------------------------------

import plotly.graph_objects as go

fig = go.Figure(\
                data = 
                 [go.Candlestick
                  (
                    x = df.Date,
                    open = df.Open,
                    high = df.High,
                    low = df.Low,
                    close = df.Close
                )])

fig.show()
