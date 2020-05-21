class Stack:
  def __init__(self):
    self.length = 0
    self.stack = []

  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack

  def push(self, data):
    # write your code to add data following LIFO and return the Stack
    self.stack = [data] + self.stack
    self.length += 1
  def pop(self):
    # write your code to removes the data following LIFO and return the Stack
    self.stack.pop(0)
    self.length -= 1

  def size(self):
    return self.length
    
s = Stack()
a = 'a'
b = 'b'
c = 'c'
d = 'd'

print(s.stack)
s.push(a)
s.push(b)
s.push(c)
s.push(d)
print(s.stack, s.length)
s.pop()
print(s.stack, s.length)