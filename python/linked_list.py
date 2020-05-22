class LinkList:

  def __init__(self):
    self.head = None

  def __str__(self):
    return_list = []
    current = self.head
    while current:
      return_list.append(current.data)
      current = current.next
    return ', '.join(str(data) for data in return_list)

  def add(self, data):
    insert = Node(data)
    if self.head:
      current = self.head
      while current.next:
        current = current.next
      current.next = insert
    else:
      self.head = insert

  def remove(self, data):
      previous = None
      if self.head.data == data:
        self.head.next.data = self.head.data
        self.head = self.head.next
      current = self.head
      while True:
        if current.data == data:
          previous.next = current.next
          break
        else:
          previous = current
          current = current.next
          

  def get(self, element_to_get):
    current = self.head
    if current.data == element_to_get:
        return current
    while True:
      if current.data == element_to_get:
        return current
      else:
        current = current.next

# ----- Node ------
class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

