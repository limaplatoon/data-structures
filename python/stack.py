class Stack:
  def __init__(self):
    self.stack = []
    self.total = len(self.stack)
    
  def push(self, data):
    self.stack.append(data)

  def pop(self):
    self.stack.pop()

  def size(self):
    return self.total
    
    


