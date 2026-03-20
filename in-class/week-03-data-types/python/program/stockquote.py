# Logs
# - [2026/03/20]
#   Read the stockprice of a specific tick. We use yfinance for short code
#   Scraping manually needs some knowledge of dynamic web page 

import sys
import yfinance as yf

def price_of(stock_symbol):
  ticker = yf.Ticker(stock_symbol)
  current_price = ticker.info.get("currentPrice")
  return current_price

def _main():
  stock_symbol = sys.argv[1].upper()
  price = price_of(stock_symbol)
  print(f"{price:.2f}")


if __name__ == "__main__": _main()