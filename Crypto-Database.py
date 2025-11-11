# List of cryptocurrency coins dictionaries:

crypto_coin = [
{
"name": "Bitcoin",
"ticker": 'BTC',
"price": 35870.86,
"24h_change": 1.48,
"volume": 670552492185,
"supply": 18721781,
"category": 'CURRENCY'
},

{
"name": "Ethereum",
"ticker": 'ETH',
"price": 2422.80,
"24h_change": 0.05,
"volume": 281073942766,
"supply": 116083174,
"category": 'PLATFORM'
},

{
"name": "Cardano",
"ticker": 'ADA',
"price": 1.63,
"24h_change": 10.26,
"volume": 51951358766,
"supply": 31948309441,
"category": 'PLATFORM'
},

{
"name": "Binance Coin",
"ticker": 'BNB',
"price": 331.21,
"24h_change": 6.08,
"volume": 50829735875,
"supply": 153432897,
"category": 'EXCHANGE'
},

{
"name": "XRP",
"ticker": 'XRP',
"price": 5.00,
"24h_change": 7.39,
"volume": 40594034312,
"supply": 46143602688,
"category": 'CURRENCY'
},

{
"name": "Dogecoin",
"ticker": 'DOGE',
"price": 0.31,
"24h_change": 2.11,
"volume": 39593068555,
"supply": 129813129789,
"category": 'CURRENCY'
}
]
#--------------------------------------------------

dogecoin = crypto_coin[3]

print(dogecoin)
print()
#--------------------------------------------------

import pandas as pd
dogecoin = crypto_coin[3]

d = pd.Series(dogecoin)
print(d)
print()
#--------------------------------------------------

if 'PLATFORM' in crypto_coin[3]['category']:
    print('True')
else:
    print('False')
    
    
#THE END
