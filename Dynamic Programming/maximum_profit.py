#  File: maximum_profit.py

#  Description:  Real Estate Investemnt Assigment

#  Student Name: Samuel Kalisch

#  Student UT EID: sk54596

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: April 23, 2022

#  Date Last Modified:April 26, 2022

import sys

def maximum_profit(money, num_houses, prices, increase):
  
  # calculates minimum price
  min_price = min(prices)
  
  #profits by each house 
  profits = [prices[i]*(increase[i]) for i in range(num_houses)]
  
  # create dynamic programming table 
  mtx = [[0 for i in range(money - min_price +1)] for i in range(num_houses)]

  # update table
  for i in range(num_houses):
    for w in range(money - min_price +1):
      
      # for the first iteration 
      if i == 0: mtx[0][w] = profits[0] if prices[0] <= (w + min_price ) else 0
      
      # for every other iteration
      else:
        temp = mtx[i-1][w - prices[i]] if prices[i] <= w else 0
        mtx[i][w] = max(mtx[i-1][w],profits[i] + temp) if prices[i] <= w + min_price  else  mtx[i-1][w]   
  
  print_mtx(mtx)
  return mtx[i][w]/100

def print_mtx(mtx):
  for line in mtx:
    for item in line:
      print(format(int(item), "<3"), end = ' ')
    print()
  
def main():
	# Reads the money and the number of houses
	money = int(sys.stdin.readline().strip())
	num_houses = int(sys.stdin.readline().strip())

	# The third line is a list of house prices in million dollar which is a list of \textit{integer numbers} (Consider that house prices can be an integer number in million dollar only).
	prices = sys.stdin.readline().strip().split(",")
	for i in range(0, len(prices)):
		prices[i] = int(prices[i])
	
	# read the number of vertices
	increase = sys.stdin.readline().strip().split(",")
	for i in range(0, len(increase)):
		increase[i] = float(increase[i])

	# Add your implementation here .... 
	result =  maximum_profit(money, num_houses, prices, increase)

	# Add your functions and call them to generate the result. 
	print(result)

if __name__ == '__main__':
	main()
