#!/usr/bin/python

import argparse

def find_max_profit(prices):
  if type(prices) != list:
    return "Enter a list of stock prices"

  current_min_price_so_far = 0
  max_profit_so_far = 0
  maximumIndex = 0

  for i in range(prices):

    if max_profit_so_far <= prices[i]:
      max_profit_so_far = prices[i]
      maximumIndex = i

    if i <= maximumIndex and current_min_price_so_far >= prices[i]:
      current_min_price_so_far = prices[i]

  profit = max_profit_so_far - current_min_price_so_far


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))