#  File: TestBinaryTree.py

#  Description: Binary tree with a range, get_level, left_view, and sum_leaf_nodes methods

#  Student Name: Samuel Kalisch Yanez

#  Student UT EID: sk54596

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: March 22, 2022

#  Date Last Modified: March 23, 2022

import sys

class Node (object):
    # constructor
  def __init__(self, data):
    self.data = data
    self.lChild = None
    self.rChild = None
        
  def is_leaf(self):
    return self.lChild == None and self.rChild == None

  def print_node(self, level=0):
    if self.lChild != None:
      self.lChild.print_node(level + 1)

    print(' ' * 3 * level + '->', self.data)

    if self.rChild != None:
      self.rChild.print_node(level + 1)

  def get_height(self):
    if self.lChild != None and self.rChild != None:
      return 1 + max(self.lChild.get_height(), self.rChild.get_height())
    elif self.lChild != None:
      return 1 + self.lChild.get_height()
    elif self.rChild != None:
      return 1 + self.rChild.get_height()
    else:
      return 1

class Tree(object):
  # constructor
  def __init__(self):
    self.root = None

  def print(self, level):
    self.root.print_node(level)

  def get_height(self):
    return self.root.get_height()

  # Inserts data into Binary Search Tree and creates a valid BST
  def insert(self, data):
    new_node = Node(data)
    if self.root == None:
      self.root = new_node
      return
    else:
      parent = self.root
      curr = self.root
      # finds location to insert new node
      while curr != None:
        parent = curr
        if data < curr.data:
          curr = curr.lChild
        else:
          curr = curr.rChild
      # inserts new node based on comparision to parent node
      if data < parent.data:
        parent.lChild = new_node
      else:
        parent.rChild = new_node
      return

  # Helper function, gets the min of the tree
  def get_min(self):
    current = self.root
    while current.lChild != None:
      current = current.lChild
    return int(current.data)
  
  # Helper function, gets the max of the tree
  def get_max(self):
    current = self.root
    while current.rChild != None:
      current = current.rChild
    return int(current.data)
    
  # Returns the range of values stored in a binary search tree of integers.
  # The range of values equals the maximum value in the binary search tree minus the minimum value.
  # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
  def range(self):

    #if root is empty
    if self.root == None: return 
    
    #if root is a leaf (one value only)
    if self.root.is_leaf(): return 0

    return self.get_max() - self.get_min()

  # Returns a list of nodes at a given level from left to right
  def get_level(self, level=0, current = False, current_level = 0):
    #initiates current at the begininng to the root
    if current == False: current  = self.root
    
    #if it is empty returns none
    if current == None: return []
    
    #if it is one the level needed
    if level == current_level: return [current]
    
    left = self.get_level(level, current.lChild, current_level+1)
    right = self.get_level(level, current.rChild, current_level+1)
    
    return left + right

  # Returns the list of the node that you see from left side
  # The order of the output should be from top to down
  def left_side_view(self):
    lst = []
    #gets the first iten of each level
    for level in range(self.get_height()):
      lvl = self.get_level(level)
      lst.append(lvl[0].data)
    return lst
 
 
  # returns the sum of the value of all leaves.
  # a leaf node does not have any children.
  def sum_leaf_nodes(self, current = False):
    #initiates current at the begininng to the root
    if current == False: current  = self.root
    
    #if root is empty
    if current == None: return 0
    
    #if root is a leaf (one value only)
    if current.is_leaf(): return current.data

    left = self.sum_leaf_nodes(current.lChild)
    right = self.sum_leaf_nodes(current.rChild)
    
    return  left + right


def make_tree(data):
  tree = Tree()
  for d in data:
    tree.insert(d)
  return tree

# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.
def main():
  # Create three trees - two are the same and the third is different
  line = sys.stdin.readline()
  line = line.strip()
  line = line.split()
  tree1_input = list(map(int, line)) 	# converts elements into ints
  t1 = make_tree(tree1_input)
  t1.print(t1.get_height())

  print("Tree range is: ",   t1.range())
  print("Tree left side view is: ", t1.left_side_view())
  print("Sum of leaf nodes is: ", t1.sum_leaf_nodes())
  for i in range(t1.get_height()):
    print(f"Tree level {i} view is: ", t1.get_level(i))
  print("##########################")


if __name__ == "__main__":
  main()
  


