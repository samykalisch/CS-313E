class Link(object):
  ''' This class represents a link between data items only'''
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

  def __str__(self):
    return str(self.data)

class LinkedList(object):
  ''' This class implements the operations of a simple linked list'''
  def __init__ (self):
    self.first = None
    self.last = None

  def insertFirst (self, data):
    '''inset data at begining of a linked list'''
    newLink = Link(data)
    if self.first== None: self.last = newLink
    newLink.next = self.first
    self.first = newLink
    

  def insertLast (self, data):
    ''' Inset the data at the end of a linked list '''
    newLink = Link(data)
    current = self.first
    self.last = newLink

    if (current == None):
      self.first = newLink
      return
    # find the last and insert it there. 
    while (current.next != None):
      current = current.next

    current.next = newLink

  def findLink(self, data):
    ''' find to which data is the link of a given data inside this linked list'''
    current = self.first
    if (current == None):
      return None

    # searcg and find the position of the given data, the get the link if. 
    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current

  def deleteLink(self, data):
    ''' Removes the data from the list if exist and fix the link problems.'''

    current = self.first
    previous = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
    
      current = current.next
    if (current == self.last): self.last = previous
    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next

    return current


  def __str__(self):
    ls  = []
    current = self.first
    while current != None:
      ls.append(current.data)
      current = current.next
    return str(ls) 

class StackByLinkedList(object):
    
  def __init__(self):
    self.linked_list = LinkedList()
    
  # add an item to the top of the stack
  def push (self, item):
    self.linked_list.insertLast(item)

  # remove an item from the top of the stack
  def pop(self):
    current = self.linked_list.last
    if current == None: return
    return self.linked_list.deleteLink(current.data)

  
  # check what item is on top of the stack without removing it
  def peek(self):
    return self.linked_list.last
  def isEmpty(self):
    return self.linked_list.first == None
  
  def __str__(self):
    return str(self.linked_list)
  
def main():
  my_stack = StackByLinkedList()

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

