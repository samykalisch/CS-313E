#  File: Cipher.py

#  Description: crypts the first string given and decryots the second string given

#  Student Name: Samuel Kalisch Yanez

#  Student UT EID: sk54596

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: 02/01/2022

#  Date Last Modified: 02/01/2022
import math
import sys

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt( strng ):

  #gets k which is the smallest square number greater than or equal to the lenght of the string and creates a matrix of k size
  k = math.ceil(math.sqrt(len(strng)))
  message = [['*' for i in range(k)] for j in range(k)]
  
  #fills the string rotated clockwise to the string if not leaves the '*'
  for n in reversed(range(k)):
    for m in range(k):
      if strng:
        message[m][n], strng = strng[0], strng[1:]
  

  #matrix to string
  final_message = ''
  for m in range(k):
    for n in range(k):
      if message[m][n]!= '*' :
        final_message += message[m][n]
  
  return final_message
  
    
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt(strng):
  #gets k which is the smallest square number greater than or equal to the lenght of the string and creates a matrix of k size
  k = math.ceil(math.sqrt(len(strng)))
  message = [['*' for i in range(k)] for j in range(k)]
  
  #gets the numbers of spaces missing and the number of incomplete columns 
  missing, incomplete = k**2 - len(strng), math.ceil((k**2 - len(strng))/k)
  
  #fills the sting left to right skiping the columns which are empty
  for n in range(k):
    for m in range(k):
      #skips the columns which are completly empty
      if m > incomplete-1:  
        message[n][m], strng= strng[0], strng[1:]
      #fills the incomplete columns top to button and skips the missing parts of the column
      elif m == incomplete -1:
        if n < k*(m+1) - missing:
          message[n][m], strng= strng[0], strng[1:]
  
  #matrix to string
  final_message = ''   
  for n in reversed(range(k)):
    for m in range(k):
      if message[m][n]!= '*' :
        final_message += message[m][n]
   
  return final_message
 
def main():
  # read the strings P and Q from standard inputs 
  p = sys.stdin.readline().strip()
  q = sys.stdin.readline().strip()
  # encrypt the string P
  P_encrypted = encrypt(p)
  # decrypt the string Q
  Q_decrypted =decrypt(q)
  # print the encrypted string of P
  print(encrypt(p))
  # and the decrypted string of Q
  print(Q_decrypted)

if __name__ == "__main__":
  main()

  
