class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insertAtEnd(self,data):
    newNode = Node(data)

    if self.head:
      current = self.head
      while(current.next):
        current = current.next
      
      current.next = newNode
    
    else:
      self.head = newNode
    
  def insertAtFront(self,data):
    newNode = Node(data)
    newNode.next = self.head
    self.head = newNode
      
  def deleteNode_byKey(self,key):
    if self.head is None:
      print("LinkedList is empty")
      return
    
    current = self.head

    while current.next:
      if current.next.data == key:
        current.next = current.next.next
        return
      current = current.next 

    print("Value not found")
   

  def searchNode(self,data):
    self.data = data
    if self.head is None:
      print("LinkedList is empty")
      return
    i = 0
    current = self.head
    while current:
      if current.data == data:
        i = i + 1
       
      current = current.next

    if i>0 : 
      print(f"{data} is in the LinkedList")
    else:
      print(f"{data} is not in the LinkedList")
      


  def traverse(self):

    temp = self.head
    if temp is None:
      print("Empty LinkedList!!!")
      
    
    else:
      while temp:
        print(temp.data, end="-->")
        temp = temp.next
      
    print()  

L1 = LinkedList()
# L1.insertAtEnd(15)
# L1.insertAtEnd(25)
# L1.insertAtEnd(70)
# L1.insertAtEnd(90)
# L1.traverse()

L1.insertAtFront(9)
L1.insertAtFront(10)

L1.insertAtFront(4)
L1.insertAtFront(6)
L1.traverse()

L1.deleteNode_byKey(4)
L1.traverse()

L1.searchNode(9)