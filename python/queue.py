class Queue:
  def __init__(self):
    self.queue = []
    self.total = len(self.queue)
  
  def enqueue(self, value):
    self.queue.insert(0, value)
    self.total = len(self.queue)

  def dequeue(self):
    self.queue.pop(-1)

  def size(self):
    return self.total



