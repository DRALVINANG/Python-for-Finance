import pandas as pd
import plotly.graph_objects as go

# Stock data URLs
stock_data_urls = {
    "AAPL": "https://raw.githubusercontent.com/DRALVINANG/Streamlit/refs/heads/main/datasets/aapl_2024.csv",
    "TSLA": "https://raw.githubusercontent.com/DRALVINANG/Streamlit/refs/heads/main/datasets/tsla_2024.csv",
    "AMZN": "https://raw.githubusercontent.com/DRALVINANG/Streamlit/refs/heads/main/datasets/amzn_2024.csv",
    "MSFT": "https://raw.githubusercontent.com/DRALVINANG/Streamlit/refs/heads/main/datasets/msft_2024.csv",
    "NVDA": "https://raw.githubusercontent.com/DRALVINANG/Streamlit/refs/heads/main/datasets/nvda_2024.csv",
    "INTC": "https://raw.githubusercontent.com/DRALVINANG/Streamlit/refs/heads/main/datasets/intc_2024.csv"
}

# Select stock (AAPL for this example)
selected_stock = "AAPL"

# Fetch the data
stock_data_url = stock_data_urls[selected_stock]
stock_data = pd.read_csv(stock_data_url)

# Convert the 'Date' column to datetime and set it as the index
stock_data['Date'] = pd.to_datetime(stock_data['Date'])
stock_data.set_index('Date', inplace=True)

# Create the candlestick chart
candlestick = go.Figure(data=[go.Candlestick(
    x=stock_data.index,
    open=stock_data["Open"],
    high=stock_data["High"],
    low=stock_data["Low"],
    close=stock_data["Close"]
)])

# Update the chart layout and axes
candlestick.update_xaxes(
    title_text="Date",
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1M", step="month", stepmode="backward"),
            dict(count=6, label="6M", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1Y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

candlestick.update_layout(
    title=f"{selected_stock} Share Price (2013-2024)",
    yaxis_title=f"{selected_stock} Close Price",
    yaxis=dict(tickprefix="$")
)

# Display the chart
candlestick.show()
