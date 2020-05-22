class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self):
    self.head = Node('HEAD')
    self.size = 0

  def add(self, data):
    # write your code to ADD an element to the Linked List
    new_node = Node(data)
    #find the starting point
    current_position = self.head

    #find our way to the end
    while current_position.next:
      previous = current_position
      current_position = previous.next

    #now at the end lets make sure the previous node knows we are here
    current_position.next = new_node
    self.size += 1

  def remove(self, target_data):
    # write your code to REMOVE an element from the Linked List
    current_position = self.head
    while current_position.data != target_data:
      previous = current_position
      current_position = previous.next
    previous.next = current_position.next
    self.size -1

  def get(self, element_to_get):
    # write you code to GET and return an element from the Linked List
    if element_to_get <= self.size:
      current_position = self.head
      current_element = 0
      while current_element < element_to_get:
        previous = current_position
        current_position = previous.next
        current_element +=1
      return current_position.data


# ----- Node ------
class Node:
  # store your DATA and NEXT values here
  def __init__(self, data):
    self.data = data
    self.next = None


