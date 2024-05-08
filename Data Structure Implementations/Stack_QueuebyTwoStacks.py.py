class Stack (object):

  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append(item)

  # remove an item from the top of the stack
  def pop(self):
    if(not self.isEmpty()):
      return self.stack.pop()
    else:
      return None

  # check what item is on top of the stack without removing it
  def peek(self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size(self):
    return (len(self.stack))

  # a string representation of this stack. 
  def __str__(self):
    return str(self.stack)
    
class QueueBytwoStack(object):
    
  def __init__(self):
    self.stack_1 = Stack()
    self.stack_2 = Stack()
    
  def enqueue (self, item):
    self.stack_1.push(item)

  def dequeue (self):
    
    if self.stack_1.isEmpty(): return
    
    while not self.stack_1.isEmpty():
      self.stack_2.push(self.stack_1.pop())
    
    deq = self.stack_2.pop()
    
    while not self.stack_2.isEmpty():
     self.stack_1.push(self.stack_2.pop())
    
    return deq
  
    # a string representation of this stack.
  def __str__(self):
    return str(self.stack_1)
  
def main():
  my_queue = QueueBytwoStack()

  # enqueue 10
  my_queue.enqueue(10)
  print(my_queue)

  # enqueue 18
  my_queue.enqueue(18)
  print(my_queue)


  # enqueue 1024
  my_queue.enqueue(1024)
  print(my_queue)


  # dequeue()
  print("Dequeue ", my_queue.dequeue())
  print("Dequeue ", my_queue.dequeue())
  print("Dequeue ", my_queue.dequeue())
  print("Dequeue ", my_queue.dequeue())


if __name__ == '__main__':
  main()
