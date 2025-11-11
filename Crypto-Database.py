import pandas as pd
import plotly.graph_objects as go

# Cryptocurrency data
crypto_coin = [
    {
        "name": "Bitcoin",
        "ticker": 'BTC',
        "price": 35870.86,
        "24h_change": 1.48,
        "volume": 670552492185,
        "supply": 18721781,
        "category": 'CURRENCY',
        "csv_url": "https://raw.githubusercontent.com/DRALVINANG/Streamlit/refs/heads/main/datasets/btc_2024.csv"
    },
    {
        "name": "Ethereum",
        "ticker": 'ETH',
        "price": 2422.80,
        "24h_change": 0.05,
        "volume": 281073942766,
        "supply": 116083174,
        "category": 'PLATFORM',
        "csv_url": "https://raw.githubusercontent.com/DRALVINANG/Streamlit/refs/heads/main/datasets/eth_2024.csv"
    }
]

# Prompt the user to select a coin
print("Available coins: BTC (Bitcoin), ETH (Ethereum)")
coin = input("Which coin would you like to work with? ").upper()

# Find the selected coin from the list
selected_coin = next((coin for coin in crypto_coin if coin['ticker'] == coin), None)

if selected_coin is None:
    print(f"Invalid coin selected: {coin}. Please choose from the available options (BTC or ETH).")
else:
    print(f"Selected Coin: {selected_coin['name']}")
    print("=" * 50)

    # Display coin details
    print("Coin Details:")
    print(f"Name: {selected_coin['name']}")
    print(f"Ticker: {selected_coin['ticker']}")
    print(f"Price: ${selected_coin['price']}")
    print(f"24h Change: {selected_coin['24h_change']}%")
    print(f"Volume: {selected_coin['volume']}")
    print(f"Supply: {selected_coin['supply']}")
    print(f"Category: {selected_coin['category']}")
    
    print("\n" + "=" * 50)

    # Get historical data
    coin_data = pd.read_csv(selected_coin['csv_url'])
    print("Recent Price Data:")
    print(coin_data[['Date', 'Open', 'High', 'Low', 'Close']].tail())

    print("\n" + "=" * 50)

    # Check conditions
    print("Condition Check:")
    condition1 = selected_coin['category'] == 'PLATFORM'
    print(f"Category is PLATFORM: {condition1}")

    condition2 = selected_coin['24h_change'] > 5
    print(f"24h Change > 5%: {condition2}")

    print("\n" + "=" * 50)

    # Create candlestick chart
    candlestick = go.Figure(data=[go.Candlestick(
        x=coin_data['Date'],
        open=coin_data["Open"],
        high=coin_data["High"],
        low=coin_data["Low"],
        close=coin_data["Close"]
    )])

    candlestick.update_layout(
        title=f"{selected_coin['ticker']} Candlestick Chart"
    )

    candlestick.update_yaxes(title_text=f"{selected_coin['ticker']} Price")

    # Show the chart
    candlestick.show()

    # Coin history
    coin_history = {
        "BTC": "Bitcoin is the first decentralized cryptocurrency, created in 2009 by an anonymous person (or group) known as Satoshi Nakamoto. It allows peer-to-peer transactions without the need for intermediaries, relying on blockchain technology to secure and verify transactions.",
        "ETH": "Ethereum is a decentralized platform that enables developers to build and deploy smart contracts and decentralized applications (dApps). Launched in 2015, it introduced the concept of programmable money and is the second-largest cryptocurrency by market capitalization."
    }

    print(f"\nCoin History for {selected_coin['ticker']}:")
    print(coin_history[selected_coin['ticker']])
