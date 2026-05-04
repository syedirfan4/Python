class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self,data):
    newNode = Node(data)

    if self.head:
      current = self.head
      while(current.next):
        current = current.next
      
      current.next = newNode
    
    else:
      self.head = newNode
    

  def traverse(self):

    temp = self.head
    if temp is None:
      print("Empty LinkedList!!!")
      
    
    else:
      while temp:
        print(temp.data, end="-->")
        temp = temp.next

L1 = LinkedList()
L1.insert(15)
L1.insert(25)
L1.insert(70)
L1.insert(90)
L1.traverse()
    