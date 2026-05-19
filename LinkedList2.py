class node:
  def __init__(self,data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self,data):
    # self.data = data
    newNode = node(data) 

    if self.head is None :
      self.head = newNode
      return
    
    last = self.head
    while(last.next):
      last = last.next

    last.next = newNode

  def insert_at_beginning(self, data):
    newNode = node(data)
    newNode.next = self.head
    self.head = newNode

  def specific_loc(self,data,position):
    newNode = node(data)
    

  
  def traverse(self):
    temp = self.head
    if temp is None:
      print("Create some Node first dumbass")
      return
    while temp is not None:
      print(temp.data,end="-->")
      temp = temp.next

    print()



L1 = LinkedList()    
L1.append(25)

L1.traverse()

L1.append(29)
L1.traverse()
L1.append(90)
L1.traverse()


L1.insert_at_beginning(12)
L1.traverse()

L2 = LinkedList()
L2.append(199)
L2.append(16)
L2.traverse()
