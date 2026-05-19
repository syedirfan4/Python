class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    self.previous = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node

    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)

    self.head_node = new_head

    if self.tail_node == None:
      self.tail_node = new_head
