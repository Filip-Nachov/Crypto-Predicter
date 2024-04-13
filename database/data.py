import sqlite3

conn = sqlite3.connect('cryptocurrency.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cryptocurrencies (
        id INTEGER PRIMARY KEY,
        name TEXT,
        symbol TEXT,
        price REAL,
        market_cap REAL
    )
''')

cryptocurrencies = [
    ('Bitcoin', 'BTC', 45000.00, 845000000000),
    ('Ethereum', 'ETH', 3000.00, 350000000000),
    ('Litecoin', 'LTC', 200.00, 15000000000),
    ('Dogecoin', 'DOGE', 0.2, 25000000000),
    ('Ethereum', 'ETH', 3000.00, 350000000000),
    ('Ripple', 'XRP', 1.5, 70000000000),
    ('Cardano', 'ADA', 1.2, 40000000000),
    ('Polkadot', 'DOT', 30.0, 30000000000),
    ('Chainlink', 'LINK', 25.0, 15000000000),
    ('Binance Coin', 'BNB', 500.0, 75000000000)  
]

cursor.executemany('''
    INSERT INTO cryptocurrencies (name, symbol, price, market_cap)
    VALUES (?, ?, ?, ?)
''', cryptocurrencies)

conn.close()