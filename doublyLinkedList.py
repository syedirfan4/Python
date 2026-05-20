class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None

  def append(self,data):
    new_node = Node(data)

    curr = self.head

    if curr == None:
      self.head = new_node
      return
    
    while curr.next:
      curr = curr.next

    curr.next = new_node
    new_node.prev =curr
  
  def display(self):
    temp = self.head
    if temp is None:
      print("List is empty")
      return
    while temp:
      print(temp.data,end="-->")
      temp = temp.next
    
    print("None")
    

L1 = DoublyLinkedList()
L1.append(2)
L1.append(3)
L1.append(4)
L1.display()

print(L1.head.data)