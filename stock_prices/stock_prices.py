#!/usr/bin/python

import argparse

def find_max_profit(prices):
  #given a list, find smallest element, and the biggest element
  # find the difference ONLY IF the smaller element comes BEFORE the largest element
  #return difference
  differences = []
  for i in range(len(prices)-1,0,-1):
    for j in range(i,0,-1):
      if prices[j] < prices[i]:
        differences.append(prices[i] - prices[j])
  print("DIFF", differences)
  return max(differences)

#[10, 7, 5, 8, 11, 9] 6
#[1050, 270, 1540, 3800, 2] 3530
if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))