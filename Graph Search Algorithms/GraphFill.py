#  File: GraphFill.py

#  Description:  builds a graph, print its adjacency matrix and implementsBreadth-First Search
#                and Depth-First Search to flood fill pixels in images

#  Student Name: Samuel Kalisch

#  Student UT EID: sk54596

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: April 2, 2022

#  Date Last Modified:April 2, 2022

import os
import sys

# this enables printing colors on Windows somehow
os.system("")

# code to reset the terminal color
RESET_CHAR = "\u001b[0m"
# color codes for the terminal
COLOR_DICT = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m"
}
# character code for a block
BLOCK_CHAR = "\u2588"

# Input: text is some string we want to write in a specific color
#   color is the name of a color that is looked up in COLOR_DICT
# Output: returns the string wrapped with the color code
def colored(text, color):
  color = color.strip().lower()
  if not color in COLOR_DICT:
    raise Exception(color + " is not a valid color!")
  return COLOR_DICT[color] + text

# Input: color is the name of a color that is looked up in COLOR_DICT
# prints a block (two characters) in the specified color
def print_block(color):
  print(colored(BLOCK_CHAR, color)*2, end='')

# Stack class; you can use this for your search algorithms
class Stack(object):
  def __init__(self):
    self.stack = []

  # add an item to the top of the stack
  def push(self, item):
    self.stack.append(item)

  # remove an item from the top of the stack
  def pop(self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek(self):
    return self.stack[-1]

  # check if the stack if empty
  def is_empty(self):
    return len(self.stack) == 0

  # return the number of elements in the stack
  def size(self):
    return len(self.stack)
  
  def __str__(self):
    return str([str(i) for i in self.stack])

# Queue class; you can use this for your search algorithms
class Queue(object):
  def __init__(self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue(self, item):
    self.queue.append(item)

  # remove an item from the beginning of the queue
  def dequeue(self):
    return self.queue.pop(0)

  # checks the item at the top of the Queue
  def peek(self):
    return self.queue[0]

  # check if the queue is empty
  def is_empty(self):
    return len(self.queue) == 0

  # return the size of the queue
  def size(self):
    return len(self.queue)
  
  def in_queue(self, node):
    return node in self.queues
  
  def __str__(self):
    return str([str(i) for i in self.queue])

# class for a graph node; contains x and y coordinates, a color, a list of edges and
# a flag signaling if the node has been visited (useful for serach algorithms)
# it also contains a "previous color" attribute. This might be useful for your flood fill implementation.
class ColorNode:
    # Input: x, y are the location of this pixel in the image
    #   color is the name of a color
    def __init__(self, x, y, color):
      self.color = color
      self.prev_color = color
      self.x = x
      self.y = y
      self.edges = []
      self.visited = False

    # Input: node_index is the index of the node we want to create an edge to in the node list
    # adds an edge and sorts the list of edges
    def add_edge(self, node_index):
      self.edges.append(node_index)
      self.edges.sort()

    # Input: color is the name of the color the node should be colored in;
    # the function also saves the previous color (might be useful for your flood fill implementation)
    def set_color(self, color):
      self.prev_color = self.color
      self.color = color
    
    def __str__(self):
      return f'x: {self.x}, y: {self.y}, color: {self.color} prev: {self.prev_color}, visited: {self.visited}'

# class that contains the graph
class ImageGraph:
    def __init__(self, image_size):
      self.nodes = []
      self.image_size = image_size

    # prints the image formed by the nodes on the command line
    def print_image(self):
      img = [["black" for i in range(self.image_size)] for j in range(self.image_size)]

      # fill img array
      for node in self.nodes:
        img[node.y][node.x] = node.color

      for line in img:
        for pixel in line:
          print_block(pixel)
        print()
      # print new line/reset color
      print(RESET_CHAR)

    # sets the visited flag to False for all nodes
    def reset_visited(self):
      for i in range(len(self.nodes)):
        self.nodes[i].visited = False

    # implement your adjacency matrix printing here.
    def print_adjacency_matrix(self):
      print("Adjacency matrix:")
      mtx = [[0 for i in range(len(self.nodes))] for j in range(len(self.nodes))]

      for index in range(len(self.nodes)):
        for index_2 in self.nodes[index].edges:
          mtx[index][index_2] = 1 

      for line in mtx:
        for num in line:
          print(num,end='')
        print()
      
      # empty line afterwards
      print()

    # implement your bfs algorithm here. Call print_image() after coloring a node
    # Input: graph is the graph containing the nodes
    #   start_index is the index of the currently visited node
    #   color is the color to fill the area containing the current node with
    def bfs(self, start_index, color):
      # reset visited status
      self.reset_visited()
      
      # print initial state
      print("Starting BFS; initial state:")
      self.print_image()
      
      #create queue
      queue = Queue()
      queue.enqueue(self.nodes[start_index])
      
      #visiting algorithm
      while not queue.is_empty():
        #deques and sets color
        current = queue.dequeue()
        current.set_color(color)
        
        #prints image
        self.print_image()
        
        #queues the elegible edges and marks them as visited
        for edge in current.edges:
          if self.nodes[edge].color == current.prev_color and  self.nodes[edge].color != color \
          and self.nodes[edge].visited == False:
            self.nodes[edge].visited = True
            queue.enqueue(self.nodes[edge])
        
      
    # implement your dfs algorithm here. Call print_image() after coloring a node
    # Input: graph is the graph containing the nodes
    #   start_index is the index of the currently visited node
    #   color is the color to fill the area containing the current node with
    def dfs(self, start_index, color):
      # reset visited status
      self.reset_visited()
      
      # print initial state
      print("Starting DFS; initial state:")
      self.print_image()
      
      #create stack
      stack = Stack()
    
      # mark the vertex start_index as visited and push it to stack
      self.nodes[start_index].visited = True
      stack.push(self.nodes[start_index])
      original_color = self.nodes[start_index].color
      
       #visiting algorithm
      while not stack.is_empty():
        #updates current to visted  and color
        current = stack.peek()
        current.set_color(color)
        current.visited = True 
        
        #finds a possible edge to go
        edge = self.find_edge(current,color,original_color)
        
        if edge: 
          stack.push(edge)
          #prints image
          self.print_image()
          
        else: 
          stack.pop()  
      
      #print last image
      self.print_image() 
    
    #helper function to visit eligible edge, if not false 
    def find_edge(self,current,color, original_color):
      for edge in current.edges: 
        if self.nodes[edge].color == original_color and self.nodes[edge].color != color\
          and self.nodes[edge].visited == False:
          return self.nodes[edge]
      return False

def main():
  #read data
  image_size = int(sys.stdin.readline())
  num_nodes = int(sys.stdin.readline())
  
  graph = ImageGraph(image_size)  
  
  for i in range(num_nodes): 
    data = sys.stdin.readline().strip().split(',')
    graph.nodes.append(ColorNode(int(data[0]), int(data[1]), data[2]))

  num_edges= int(sys.stdin.readline())
  for i in range(num_edges):
    edge = sys.stdin.readline().strip().split(',')
    graph.nodes[int(edge[0])].add_edge(int(edge[1]))
    graph.nodes[int(edge[1])].add_edge(int(edge[0]))
    
  # print matrix
  graph.print_adjacency_matrix()

  # run bfs
  bfs = sys.stdin.readline().strip().split(',')
  graph.bfs(int(bfs[0]), bfs[1])

  # run dfs
  dfs = sys.stdin.readline().strip().split(',')
  graph.dfs(int(dfs[0]), dfs[1])

if __name__ == "__main__":
  main()
