#  File: ExpressionTree.py

#  Description: Code that creates an expression tree with a given equation and outputs its result, 
#  prefix expression and postfix expression

#  Student Name: Samuel Kalisch 

#  Student UT EID: sk54596

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: March 10 2022

#  Date Last Modified: March 13 2022

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
  def __init__(self):
    self.stack = []

  def push(self, data):
    self.stack.append (data)

  def pop(self):
    if(not self.is_empty()):
      return self.stack.pop()
    else:
      return None

  def is_empty(self):
    return len(self.stack) == 0

class Node (object):
  def __init__ (self, data = None, lChild = None, rChild = None):
    self.data = data
    self.lChild = lChild
    self.rChild = rChild
  
  # helper function 
  # to know if a node is a leaf (no childs)
  def is_leaf(self):
    return self.lChild == None and self.rChild == None
  
  def __str__(self):
    return f'Data: {self.data}, lChild: {self.lChild.data}, rChild: {self.rChild.data}'
  
class Tree (object): 
  def __init__ (self):
    self.root = None
    
  # this function takes in the input string expr and 
  # creates the expression tree
  def create_tree (self, expr):
    stack = Stack()
    expr = expr.split(' ')
    
    self.root = Node()
    current = self.root 
  
    for s in expr:  
      
      #new left child if (
      if s == '(':
        current.lChild = Node()
        stack.push(current)
        current = current.lChild
        
      #sets data if operator
      elif s in operators:
        current.data = s
        stack.push(current)
        current.rChild = Node()
        current = current.rChild
      
      #new left child if )
      elif s == ')':
        if not stack.is_empty(): current = stack.pop()
        
      #if it is an operand
      else:
        current.data = s
        if not stack.is_empty(): current = stack.pop()
 
  # helper funtion 
  # calculates the expression given its symbol and two numbers
  def calculate(self, symbol, left, right ):
    if symbol == '+': return left + right
    if symbol == '-': return left - right
    if symbol == '*': return left * right
    if symbol == '/': return left / right
    if symbol == '%': return left % right
    if symbol == '**': return left ** right
    if symbol == '//': return left // right
    
  # this function should evaluate the tree's expression
  # returns the value of the expression after being calculated
  def evaluate (self, aNode):
    
    #base case, if the three is empty
    if aNode ==  None: return 0
    
    #base case, the node is a number
    if aNode.lChild == None and aNode.rChild == None: return aNode.data

    symbol = aNode.data
    left = float(self.evaluate(aNode.lChild))
    right = float(self.evaluate(aNode.rChild))
    
    return self.calculate(symbol,left,  right)
    
  # helper function
  # goes down left until current is a leaf and adds all those values including leafs to the string
  # it pushes all operator it went down to stack and adds them to the past operators list
  def down_left(self, pst, stack, current, strng):
    
    #while current is not a leaf goes down, if not returns
    while True :
      if current.lChild.is_leaf():
        pst += [current]
        strng += f' {current.data} {current.lChild.data}'
        return pst, current, strng
      
      strng += f' {current.data}'
      pst += [current]
      stack.push(current)
      current = current.lChild
      
  # helper function
  # if the right child is a leaf it adds it up to the srtng and goes up
  # if not it only goes to the right 
  def down_right(self, stack, current, strng):
    if current.rChild.is_leaf(): 
      strng += f' {current.rChild.data}'
      current = self.go_up( stack, current)
      return current, strng
    
    current = current.rChild
  
    return current, strng
    
  #helper function
  #goes one up one by popping the stack
  def go_up(self, stack, current):
    current = stack.pop()  
    return current
      
  # this function should generate the preorder notation of 
  # the tree's expression
  # returns a string of the expression written in preorder notation
  def pre_order (self, aNode):
    stack = Stack()
    current = aNode 
    pst = []
    strng = ''

    #if current is empty
    if current.data == None: return ''
    
    #if current is a leaf
    if current.is_leaf(): return current.data
    
    # while current is a Node
    while current != None:
      
      #if the stack is not already in the straing goes left, uses past list to know if node was already useed
      if current.lChild not in pst: pst, current, strng = self.down_left(pst, stack, current, strng)
      
      #goes right
      current, strng = self.down_right(stack, current, strng) 
      
    return strng    
    
  # helper function to concatenate 
  # returns an expression in the form: symbol left right
  def concatenate(self, symbol, left, right ):
    return f'{left} {right} {symbol}'
    
  # this function should generate the postorder notation of 
  # the tree's expression
  # returns a string of the expression written in postorder notation
  def post_order (self, aNode):
    #base case, if the three is empty
    if aNode ==  None: return ''
    
    #base case, the node is a number
    if aNode.lChild == None and aNode.rChild == None: return f'{aNode.data}'

    symbol = aNode.data
    left = self.post_order(aNode.lChild)
    right = self.post_order(aNode.rChild)
    
    return self.concatenate(symbol, left, right)
     
# you should NOT need to touch main, everything should be handled for you
def main():
  # read infix expression
  line = sys.stdin.readline()
  expr = line.strip()

  tree = Tree()
  tree.create_tree(expr)
  
  # evaluate the expression and print the result
  print(expr, "=", str(tree.evaluate(tree.root)))

  # get the prefix version of the expression and print
  print("Prefix Expression:", tree.pre_order(tree.root).strip())

  # get the postfix version of the expression and print
  print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
  main()
