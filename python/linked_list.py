class LinkList():
  def __init__(self, head=None):
    self.head = head
    self.length = 1
    print(self.head)
     # we're going to store the length of the Linked List here

  def add(self, data):
    # write your code to ADD an element to the Linked List
    self.length += 1
    #for node in range(self.length-1)
    node = self.head
    while node.next != None:
      node = node.next
    node.next = data

  def remove(self, data):
    self.length -=1
    node = self.head
    if node == data:
      self.head = node.next
    else:
      while data != node:
        previous = node
        node = node.next
      if node.next == None:
        previous.next = None
      else:
        previous.next = node.next

  def get(self, element):
    node = self.head
    for index in range(self.length-1):
      if node == element:
        return index
      else:
        node = node.next


# ----- Node ------
class Node:
    def __init__(self, value):
      self.value = value
      self.next = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

test = LinkList(a)
test.add(b)
test.add(c)
test.add(d)


print(test.head.value)
print(test.head.next.value)
print(test.head.next.next.value)
print(test.head.next.next.next.value)

print(test.get(c))
print('-'*25)

# print(test.head.value)
# print(test.head.next.value)
# print(test.head.next.next.value)
# print(test.head.next.next.next.value)