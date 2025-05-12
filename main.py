from flask import Flask, request, render_template, redirect, url_for
from api.request import get_stock_data
app = Flask(__name__)

@app.route("/")
def homepage():
    tickers = ["AZUL4", "CRFB3", "HAPV3", "COGN3", "B3SA3", "ITSA4", "PETR4"]
    token = "dPfxHbd2pub9wVrtzbQ5AA"
    acoes = []
    for ticker in tickers:
        verde= get_stock_data(ticker, token)
        if verde:
           acoes.append(verde)

    return render_template("index.html", acoes=acoes)

if __name__ == '__main__':
    app.run(debug=True)