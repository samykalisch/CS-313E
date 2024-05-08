#  File: Josephus.py

#  Description: Assigment on linked circular list on the legend of the last soldier remaining, Josephus

#  Student Name: Samuel Kalisch

#  Student UT EID: sk54596

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: March 01 2022

#  Date Last Modified: March 01 2022
import sys

class Link(object):
  def __init__(self, data, nxt= None, previous= None):
    self.data = data
    self.next = nxt
    self.previous = previous 
    
  def __str__(self):
    #return f'{self.previous.data}<---{self.data}--->{self.next.data}'
    return f'{self.data}'
  
class CircularList(object):
  # Constructor
  def __init__ ( self ):
    self.first = None
    self.last = None
    
  # Insert an element (value) in the list
  def insert ( self, data ):
    newLink = Link(data)

    if self.first != None:
      newLink.next = self.first 
      newLink.previous = self.last   
      self.first.previous = newLink
      self.last.next = newLink 
  
    else: 
      self.first = newLink
        
    self.last = newLink
    
  # Find the Link with the given data (value)
  # or return None if the data is not there
  def find ( self, data ):
    current = self.first
    if current == None: return 
    
    while current.data != data:
      current = current.next
      
      #if it cycled once it returns or if it only one element
      if current== None or current == self.first: return
      
    return current 
      
  # Delete a Link with a given data (value) and return the Link
  # or return None if the data is not there
  def delete ( self, data ):
    current = self.first
    if current == None: return 
    
    while current.data != data:
      current = current.next
      
      #if it cycled once it returns or if it only one element
      if current== None or current == self.first: return
      
    #if current is not the only element
    if current != self.first and current !=self.last:
      current.next.previous = current.previous
      current.previous.next = current.next
    
    #replaces first and/or last in case current is
    if current == self.first: self.first = current.next
    if current == self.last: self.last = current.previous
    
    #removes current pointers
    current.next, current.previous = None, None
    
    return current
        
  # Delete the nth Link starting from the Link start
  # Return the data of the deleted Link AND return the
  # next Link after the deleted Link in that order
  def delete_after ( self, start, n ):
    current = start
    if current == None: return None, None
    if current.next == None: return current, None
    
    for i in range(n-1):
      current = current.next
      
    current.next.previous = current.previous
    current.previous.next = current.next
    
    #replaces first and/or last in case current is
    if current == self.first: self.first = current.next
    if current == self.last: self.last = current.previous
    
    #removes current pointers and stores next
    nxt = current.next
    current.next, current.previous = None, None
    
    return current, nxt
  
  # Return a string representation of a Circular List
  # The format of the string will be the same as the __str__
  # format for normal Python lists
  
  def __str__ (self):
    current = self.first
    ls = []
    
    if current == None: return '[]'

    while True:
      ls.append(int(str(current)))
      #ls.append(str(current))    
      if current == self.last:
        return str(ls)
      current = current.next
      
def main():
  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int(line)

  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int (line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int (line)

  # makes the group of intial soldiers and finds the start soldier
  soldiers_alive = CircularList()
  [soldiers_alive.insert(i)for i in range(1,num_soldiers+1)]
  next_soldier =  soldiers_alive.find(start_count)
  
  #iterates until all the soldiers are dead
  for i in range(num_soldiers):
    dead, next_soldier = soldiers_alive.delete_after(next_soldier, elim_num)
    print(dead)
  
if __name__ == "__main__":
  main()

