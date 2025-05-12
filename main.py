from api.request import get_stock_data
from banner.criacao import generate_html

TOKEN = "dPfxHbd2pub9wVrtzbQ5AA"
TICKERS = ["CRFB3", "AZUL4", "HAPV3", "COGN3", "B3SA3", "ITSA4", "PETR4"]

for ticker in TICKERS:
    stock_data = get_stock_data(ticker, TOKEN)
    if stock_data:
        generate_html(stock_data, f"banner_{ticker}.html")