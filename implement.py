class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList():
  def __init__(self):
    self.head = None
   
  def append(self, value):
    if self.head = None:
      self.head = Node(value)
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = Node(value)
  
  def show(self):
    current = self.head
    while curren.next:
      print(current.data)
      current = curren.next
      
  def length(self):
    lenght = 0
    current = self.head
    while current.next:
      length += 1
      current = current.next
   print(length)
  
  def element(self, position):
    i = 0
    current = self.head
    while current.next:
      if i == position:
        return element.data
      current = current.next
      i += 1
    return None 
