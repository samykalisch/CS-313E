#  File: Work.py

#  Description: Assigment of binary and linear search for a student's productivity

#  Student Name: Samuel Kalisch

#  Student UT EID: sk54596

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: February 22 2022

#  Date Last Modified: February 25 2022
import sys
import time
import math

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
  count = 0 
  p = 0

  while v//k**p != 0:
    count += v//k**p
    p+=1
  return count

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
  for v in range(1,n+1):
    if sum_series(v,k) >= n:
      return v

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k, low = 0, high = 0):
  #set high to n if starting and mid as averge
  if high == 0: high = n
  mid = math.ceil((high+low)/2)
  
  #gets the number of lines capable for mid and one before 
  lines_capable = sum_series(mid,k)
  lines_capable_previous = sum_series(mid-1,k)
  
  #if only three left and answer is low, this is done beacuse it uses ceiling and otherwise never ends
  if mid == 2 and lines_capable_previous > n:
    return low
  
  #if capable is bigger or equal to lines needed and one before is not the option
  elif lines_capable >= n and lines_capable_previous < n:
    return mid
  
  #if lines not enough
  elif lines_capable < n:
    return binary_search(n,k,mid,high)
  
  #if lines too many
  elif lines_capable >n:
    return binary_search(n,k,low,mid) 

def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()
def test():
  print(binary_search(3,4))
if __name__ == "__main__":
  main()
  
