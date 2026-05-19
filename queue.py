class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
  
  def enqueue(self,data):
    newNode = Node(data)
    if self.rear is None:
      self.front = self.rear = newNode
      return
    self.rear.next = newNode
    self.rear = newNode

  def dequeue(self):
    if self.front is None:
      print("Queue is Empty")
      return None
    self.front = self.front.next

    if self.front is None:
      self.rear = None
    # self.front = self.front.next 

  def peek(self):
    pass

  def printQueue(self):
    temp = self.front

    while temp:
      print(temp.data,end="-->>")
      temp = temp.next
   
    
    print()

  def peek(self):
    if self.front is None:
      print("Queue has no element in it!!")
      return
    temp = self.front.data
    print(temp)

L1 = Queue()
L1.enqueue(24)
L1.enqueue(98)
L1.enqueue(66)

L1.printQueue()

L1.dequeue()
L1.printQueue()

L1.peek()