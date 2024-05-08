#  File: DNA.py

#  Description: Program that reads a file and prints the longest common subsequence
#               of each pair of strands.

#  Student Name: Samuel Kalisch Yanez

#  Student UT EID:sk54596

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: Tuesday 18, 2022

#  Date Last Modified:Tuesday 18, 2022

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.

import sys

def longest_subsequence(s1, s2):
  ls = []
  mx = 0

  #goes through every substring in s2 bigger than 2 chars
  for i in range(len(s2)-1):
    for j in range(i+2,len(s2)+1):
        
      #checks if it is in s1 and not in the list already
      if s2[i:j] in s1 and s2[i:j] not in ls:
          
        #adds if same size and sorts
        if len(s2[i:j])== mx:
          ls.append(s2[i:j])
          ls.sort()
        #empties list and sets to the substring if bigger
        elif len(s2[i:j])>mx:
          ls = [s2[i:j]]
          mx = len(s2[i:j])
          
  return ls
          
           
     
def main():

  # read the data
  # for each pair
  for i in range(int(sys.stdin.readline())):
    # call longest_subsequence
    ls = longest_subsequence(sys.stdin.readline().upper(),sys.stdin.readline().upper())
    # write out result(s)
    if ls:
      for s in ls:
          print(s)
    else:
      print('No Common Sequence Found', end = '\n')
  # insert blank line
    print()

if __name__ == "__main__":
  main()
