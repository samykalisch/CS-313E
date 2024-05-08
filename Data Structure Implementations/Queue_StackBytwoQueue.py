class Queue(object):
  '''Queue implements the FIFO principle.'''
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    if(not self.isEmpty()):
      return self.queue.pop(0)
    else:
      return None
    
  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)
  
  # a string representation of this stack.
  def __str__(self):
    return str(self.queue)
  
class StackBytwoQueue(object):
    
  def __init__(self):
    self.queue_1 = Queue()
    self.queue_2 = Queue()
    
  # add an item to the top of the stack
  def push (self, item):
    if self.queue_1.isEmpty(): return self.queue_1.enqueue(item)
    
    size = self.queue_1.size()
    for i in range(size):
      self.queue_2.enqueue(self.queue_1.dequeue())
    
    self.queue_1.enqueue(item)
    
    for i in range(size):
      self.queue_1.enqueue(self.queue_2.dequeue())
  
     
     

  # remove an item from the top of the stack
  def pop(self):  
    return self.queue_1.dequeue()

  # check what item is on top of the stack without removing it
  def peek(self):
    if self.queue_1.isEmpty(): return None
    
    size = self.queue_1.size()
    for i in range(size):
      item = self.queue_1.dequeue()
      self.queue_2.enqueue(item)
      
      if self.queue_2.size()==1: last= item
    
    for i in range(size):
      self.queue_1.enqueue(self.queue_2.dequeue())

    return last
  
  def isEmpty (self):
    return self.queue_1.isEmpty()
  
  def __str__(self):
    ls = []
    for i in range(self.queue_1.size()):
      item = self.queue_1.dequeue()
      self.queue_1.enqueue(item)
      ls.append(item)
    return str(ls[::-1])
  
def main():
  my_stack = StackBytwoQueue()

  # Push 10
  my_stack.push(10)
  print(my_stack)

  # Push 18
  my_stack.push(18)
  print(my_stack)


  # Push 1024
  my_stack.push(1024)
  print(my_stack)


  # pop() 
  print("pop()  ", my_stack.pop())


  # peek()
  print("peak()  ", my_stack.peek())


  # isEmpty()
  print("isEmpty()   ", my_stack.isEmpty())

  print("pop()  ", my_stack.pop())
  print("pop()  ", my_stack.pop())
  print("pop()  ", my_stack.pop())
  print("isEmpty()   ", my_stack.isEmpty())
if __name__ == '__main__':
  main()

