#  File: Spiral.py

#  Description: creats a spiral and gives the adjacent sums of number in the spiral given by the imput.

#  Student Name: Samuel Kalisch Yanez

#  Student UT EID: sk54596

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: 01/25/2022

#  Date Last Modified: 01/25/2022

import sys

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral(n):
  #assigns origin and number of outer layers
  num_layers = n//2
  origin = n//2

  #creates a spiral of 1's and a list of the numbers needed,  2*num_layers+ 1  elimminates even numbers
  spiral = [[1 for i in range(2*num_layers+ 1)]for i in range(2*num_layers+ 1)]
  numbers = [i for i in range(2,(2*num_layers+ 1)**2+1)]
  
  #for every layer in the spiral
  for layer in range(1,num_layers+1):
  
    #for the right side 
    for index in range(-layer+1, layer+1):
      spiral[origin+index][origin+layer] = numbers.pop(0)
  
    #for the bottom 
    for index in range(-layer+1, layer+1):
      spiral[origin+layer][origin-index]= numbers.pop(0)

    #for the left side
    for index in range(-layer+1, layer+1):
      spiral[origin-index][origin-layer]= numbers.pop(0)
    
    #for the top
    for index in range(-layer+1, layer+1):
      spiral[origin-layer][origin+index] = numbers.pop(0)

  return spiral
  
    
# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, number):
  #finds the coodrinate (n,m) in where the number is; if empty list returns 0
  coord = list(filter(None, [ (n,m) if spiral[n][m] == number else None for n in range(len(spiral)) for m in range(len(spiral))]))
  if not coord:
    return 0

  #  asseses if the coordinate is in any side, returns a list of 4 elements: 1 if not side, 0 if side
  coord = coord[0]
  limits = [int(coord[0]!= 0), int(coord[0]!= len(spiral)-1),int(coord[1]!= 0),int(coord[1]!= len(spiral)-1)]
  

  total_sum = 0
  #goes through every adjacent number from the coordenate, if a limit is detected from above it skips the whole line
  for n in range(coord[0]-limits[0], coord[0]+limits[1]+1):
    for m in range(coord[1]-limits[2], coord[1]+limits[3]+1):
      #if it is not the coordinate it sums it to the total
      if (n,m) != coord: 
        total_sum+= spiral[n][m]

  return total_sum



def main():
  # read the input file
  n = sys.stdin.readline()
  # create the spiral
  spiral = create_spiral(int(n))
  # add the adjacent numbers
  ls = sys.stdin.read().split('\n')
  for number in ls[:-1]:
    total = sum_adjacent_numbers(spiral, int(number))
    # print the result
    print(total)
  
  for line in spiral:
    for number in line:
      print(f'{number: <4}', end='')
    print()
if __name__ == "__main__":
  main()