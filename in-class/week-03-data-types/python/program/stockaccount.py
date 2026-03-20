# Logs
# - [2026/03/20] 
#   A class to track of user account of stocks in a security
#
# TODO:
# - implement buy, sell, and write (See chapter 4)

import sys

import program.stockquote as stockquote

class StockAccount(object):
  def __init__(self, filename):
    with open(filename, "r") as fp:
      data = fp.readlines()

    self._name = data[0].strip()
    self._cash = float(data[1].strip())
    self._n = int(data[2].strip())
    self._shares = [0 for _ in range(self._n)]
    self._stocks = [0 for _ in range(self._n)]

    for i in range(self._n):
      share, stock = data[3+i].strip().split()
      self._shares[i] = int(share)
      self._stocks[i] = stock


  def value_of(self):
    total = self._cash
    for i in range(self._n):
      price = stockquote.price_of(self._stocks[i])
      amount = self._shares[i]
      total += amount * price

    return total


  def buy(self, amount, symbol):
    pass


  def sell(self, amount, symbol):
    pass


  def write(self, filename):
    pass


  def write_report(self):
    print(self._name)
    total = self._cash
    for i in range(self._n):
      amount = self._shares[i]
      price = stockquote.price_of(self._stocks[i])
      total += amount * price
      print(f"{amount:4d} {self._stocks[i]:4s}", end=" ")
      print(f"{price:7.2f}   {amount*price:10,.2f}")

    print(f"{' ':18s} {'-'*12}+")
    print(f"{'Total':>18s} {total:11,.2f}")
    print(f"{'Cash':>18s} {self._cash:11,.2f}")

def _main():
  acct = StockAccount(sys.argv[1])
  acct.write_report()

if __name__ == "__main__": _main()

