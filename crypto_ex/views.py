from django.shortcuts import render
import requests

coins = {"GBP", "BTC", "SMART"}


# Serves the homepage
def index(request):
    parameters = {"prices": get_coin_exchanges()}
    return render(request, 'index.html', parameters)


# Returns the coin's exchange rate compared to every other coin
def get_coin_exchanges():
    exchanges = {}
    rates = get_coin_prices()

    for coin in coins:
        exchanges[coin] = {}
        for compare in coins:
            exchanges[coin][compare] = round(rates[coin] / rates[compare], 5)

    return exchanges


# Returns the coin's price in USD
def get_coin_prices():
    data = {}
    prices = {}

    for coin in coins:
        data[coin] = requests.get('https://coincap.io/page/' + coin).json()
        prices[coin] = data[coin]['price_usd']

    return prices
